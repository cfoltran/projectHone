import tweepy
import json
import datetime
import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from Connect import Connect

MARGIN_DAY = 1  # Value used to retrieve all tweets below it

TWEETS_PER_SEARCH = 5 # Max Value = 100
#https://developer.twitter.com/en/docs/geo/places-near-location/self.api-reference/get-geo-search

REGIONS = {
    "Île-de-France" : "f9c4cad0af2337fa",
    "Auvergne-Rhône-Alpes" : "b2652102823ca640",
    "Bourgogne-Franche-Comté" : "60c859887b142d5f",
    "Bretagne" : "57e5628aab63276b",
    "Centre-Val de Loire" : "3f5897b87d2bf56c",
    "Corse" : "0e63aaa08b0593a4",
    "Grand Est" : "590d65437809f135",
    "Hauts-de-France" : "fec0a87de4183158",
    "Normandie" : "8e0b6cfe16a8e576",
    "Nouvelle-Aquitaine" : "2f4cc128bb4fb146",
    "Occitanie" : "829cf2c4a7c5251d",
    "Pays de la Loire" : "9dc3b9da3afde6a8",
    "Provence-Alpes-Côte d'Azur" : "3da6b5ad7b0af478",
    "La Réunion" : "0ab9fd6675769ba4",
    "Martinique" : "15bddd8209796b5e",
    "Guyane" : "991b4344edc2d520",
    "Guadeloupe" : "4e9baf84e2232342",
    "Mayotte" : "2e1db4ccd414851e"
}

class TweetByRegion:
    region = ""
    hashtag = "#"
    newTweets = ""
    def __init__(self, regionSearched,hashtagSearched=None):
        self.region = regionSearched
        if hashtagSearched == None:
            self.hashtag = "*"
        else:
            self.hashtag = hashtagSearched
        # self.API Authentification
        self.api = self.initializeAPI()

#https://developers.google.com/maps/documentation/geocoding/intro?hl=fr
#https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder?hl=fr

    def retrieveTweets(self):

        # Get today date
        today = datetime.date.today()
        # Create the margin
        margin = datetime.timedelta(days=MARGIN_DAY)

        if self.region == 'Dark-Zone':
            self.newTweets = self.api.search(q="*", lang="fr", count=TWEETS_PER_SEARCH)

        return self.newTweets


    def initializeAPI(self):
        co = Connect()
        return co.authentification()


tweet = TweetByRegion("Corse")
tweet.retrieveTweets()