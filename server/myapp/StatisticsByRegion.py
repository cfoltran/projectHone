import os
import json
import pandas
import numpy as np
from TweetByRegion import TweetByRegion
from SentimentAnalyze import Sentiment

REGIONS = ["Ile-de-France", "Auvergne-Rhone-Alpes", "Bourgogne-Franche-Comte", "Bretagne", "Centre-Val_de_Loire", "Corse", "Grand_Est", "Hauts-de-France", "Normandie", "Nouvelle-Aquitaine", "Occitanie", "Pays_de_la_Loire", "Provence-Alpes-Cote_dAzur", "La_Reunion", "Martinique", "Guyane", "Guadeloupe", "Mayotte"]


class StatisticsByRegion:
    def __init__(self, region, hashtag=None):
        self.region = region
        self.hashtag = hashtag

    def getStats(self):
        if self.region == "Dark-Zone":
            t = TweetByRegion("Dark-Zone", self.hashtag)
            res = t.retrieveTweets()
            return self.resultToFrame(res, "Dark-Zone")

        elif self.region == "all":
            # We search if a json with this hashtag exists, to avoid an API request
            filename = "data/" + self.hashtag + ".json"
            if os.path.exists(filename) and os.path.isfile(filename) and os.path.getsize(filename) > 0:
                # If he exists we display all his data
                with open(filename, 'r') as f:
                    return json.load(f)
            # Else we made a request to the API
            data = pandas.DataFrame()
            for region in REGIONS:
                t = TweetByRegion(region, self.hashtag)
                res = t.retrieveTweets()
                df = self.resultToFrame(res, region)
                data = data.append(df)
            return data

        else:
            d = TweetByRegion(self.region, self.hashtag)
            res = d.retrieveTweets()
            return self.resultToFrame(res, self.region)

    def resultToFrame(self, result, region):
        totalPolarity = 0.0
        totalRT = 0
        nbTweets = 0

        for tweet in result:
            nbTweets += 1
            sentiment = Sentiment(tweet.text)
            pol = sentiment.analyze_text()
            totalPolarity += pol[0]

        arrayRT = np.array([tweet.retweet_count for tweet in result])

        for tweet in arrayRT:
            totalRT += tweet

        data = pandas.DataFrame()
        if nbTweets != 0:
            data['AverageRetweets'] = np.array([totalRT / nbTweets])
            data['AveragePolarity'] = np.array([totalPolarity / nbTweets])
        else:
            data['AverageRetweets'] = np.array([0])
            data['AveragePolarity'] = np.array([0])
        data['NumbersOfTweets'] = np.array([nbTweets])
        data['Region'] = np.array([region])
        if self.hashtag is not None:
            data['Hashtag'] = np.array([self.hashtag])
        return data
