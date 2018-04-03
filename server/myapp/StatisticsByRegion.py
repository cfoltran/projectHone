import json
import pandas
import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from TweetByRegion import TweetByRegion
from SentimentAnalyze import Sentiment


class StatisticsByRegion:
    def __init__(self, region):
        self.region = region


    def getStats(self):
        if self.region == "all":

            data = pandas.DataFrame()

            t = TweetByRegion("Ile-de-France")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Ile-de-France")
            data = data.append(df)

            t = TweetByRegion("Auvergne-Rhone-Alpes")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Auvergne-Rhone-Alpes")
            data = data.append(df)

            t = TweetByRegion("Bourgogne-Franche-Comte")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Bourgogne-Franche-Comte")
            data = data.append(df)

            t = TweetByRegion("Bretagne")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Bretagne")
            data = data.append(df)

            t = TweetByRegion("Centre-Val_de_Loire")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Centre-Val_de_Loire")
            data = data.append(df)

            t = TweetByRegion("Corse")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Corse")
            data = data.append(df)

            t = TweetByRegion("Grand_Est")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Grand_Est")
            data = data.append(df)

            t = TweetByRegion("Hauts-de-France")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Hauts-de-France")
            data = data.append(df)

            t = TweetByRegion("Normandie")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Normandie")
            data = data.append(df)

            t = TweetByRegion("Nouvelle-Aquitaine")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Nouvelle-Aquitaine")
            data = data.append(df)

            t = TweetByRegion("Occitanie")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Occitanie")
            data = data.append(df)

            t = TweetByRegion("Pays_de_la_Loire")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Pays_de_la_Loire")
            data = data.append(df)

            t = TweetByRegion("Provence-Alpes-Cote_dAzur")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Provence-Alpes-Cote_dAzur")
            data = data.append(df)

            t = TweetByRegion("La_Reunion")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "La_Reunion")
            data = data.append(df)

            t = TweetByRegion("Martinique")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Martinique")
            data = data.append(df)

            t = TweetByRegion("Guyane")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Guyane")
            data = data.append(df)

            t = TweetByRegion("Guadeloupe")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Guadeloupe")
            data = data.append(df)

            t = TweetByRegion("Mayotte")
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Mayotte")
            data = data.append(df)

            return data

        else:
            d = TweetByRegion(self.region)
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
        return data