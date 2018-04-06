import pandas
import numpy as np
from TweetByRegion import TweetByRegion
from SentimentAnalyze import Sentiment


class StatisticsByRegion:
    def __init__(self, region, hashtag=None):
        self.region = region
        self.hashtag = hashtag

    def getStats(self):
        if self.region == "Dark-Zone":

            data = pandas.DataFrame()

            t = TweetByRegion("Dark-Zone", self.hashtag)
            res = t.retrieveTweets()
            df = self.resultToFrame(res, "Dark-Zone")
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
