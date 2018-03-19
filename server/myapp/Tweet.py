import numpy as np
import json
from SentimentAnalyze import Sentiment

import tweepy
import json
import datetime
import pandas
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from Connect import Connect

MARGIN_DAY = 1  # Value used to retrieve all tweets below it
MAX_TWEETS = 4
TWEETS_PER_SEARCH = 2 # Max Value = 100


"""Classe definissant une Tweet caractérisee par :
    tweet
    author
    geoloc
    date
    sentiment
"""


class Tweet:

    """
    Constructor
    """
    def __init__(self, hashtagSearched):
        self.tweet = "#JO Trente-deux Russes non-invités font appel pour participer aux Jeux d’hiver à #Pyeongchang2018 http://lemde.fr/2C03lpF"
        self.author = "@lemondefr"
        self.geoloc = np.array([48.864716, 2.349014])
        self.date = "2014-09-26"
        self.hashtag = "#" + hashtagSearched


    """
    Method pour analyzer le sentiment d'un tweet
    """
    def sentiment_analyze_tweet(self):
        analyze = Sentiment(self.tweet)
        self.sentiment = analyze.analyze_text()

    """
    methode pour mettre le tweet dans la conformite du fichier json
    """
    def serialize(self):
        return {
            'tweet': self.tweet,
            'author': self.author,
            'geoloc': json.loads(json.dumps(self.geoloc.tolist())),
            'date': self.date,
            'sentiment': json.loads(json.dumps(self.sentiment))
        }

    def getTweetWithTime(self):
        # API Authentification
        api = self.initializeAPI()
        # Get today date
        today = datetime.date.today()

        newTweets = api.search(q=self.hashtag, lang="fr", count=3,
                               start_time=str(today) + "T00:00:00Z", end_time=str(today) + "T12:00:00Z")

        data = pandas.DataFrame()
        data['Content'] = np.array([tweet.text for tweet in newTweets])
        data['Date'] = np.array([tweet.created_at for tweet in newTweets])
        data['Retweets'] = np.array([tweet.retweet_count for tweet in newTweets])
        data['Likes'] = np.array([tweet.favorite_count for tweet in newTweets])
        data['Author'] = np.array([self.getAuthor(tweet) for tweet in newTweets])
        return data

    def getAuthor(self, tweet):
        file = tweet.author._json
        decodedfile = json.dumps(file)
        decodedfile = json.loads(decodedfile)
        name = str(decodedfile['screen_name'])
        return name

    def initializeAPI(self):
        co = Connect()
        return co.authentication()