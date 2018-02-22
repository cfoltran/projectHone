import numpy as np
import json
from SentimentAnalyze import Sentiment

"""Classe definissant une Tweet caractérisee par :
    tweet
    author
    geoloc
    date
    sentiment
"""


class Tweet():

    """
    Constructor
    """
    def __init__(self):
        self.tweet = "#JO Trente-deux Russes non-invités font appel pour participer aux Jeux d’hiver à #Pyeongchang2018 http://lemde.fr/2C03lpF"
        self.author = "@lemondefr"
        self.geoloc = np.array([48.864716, 2.349014])
        self.date = "2014-09-26"

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
