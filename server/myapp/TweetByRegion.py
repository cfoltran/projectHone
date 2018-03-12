import tweepy
import json
import datetime

import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from Credentials import *



TWEETS_PER_SEARCH = 10 # Max Value = 100
#https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-search
class TweetByRegion:
    region = ""
    hashtag = "#"
    newTweets = ""
    def __init__(self, regionSearched,hashtagSearched):
        self.region = regionSearched
        self.hashtag = "#" + hashtagSearched

#https://developers.google.com/maps/documentation/geocoding/intro?hl=fr
    def retrieveTweets(self): 
        # API Authentification
        api = self.initializeAPI()
       
        if self.region == 'France':
           self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="46.227638,2.213749,km")
          
        elif self.region == 'Alsace':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="48.31818,7.441624,km")
        
        elif self.region == 'Aquitaine':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="44.700222,-0.299579,km")
        
        elif self.region == 'Auvergne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="45.70327,3.344854,km")
            
        elif self.region == 'Basse Normandie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="48.878847,-0.515749,km")
            
        elif self.region == 'Bourgogne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="47.052505,4.383721,km")
        
        elif self.region == 'Bretagne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="48.202047,-2.932644,km")
           
        elif self.region == 'Centre':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="47.751569,1.675063,km")
        
        elif self.region == 'Champagne-Ardenne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="48.793409,4.472525,km")
           
        elif self.region == 'Corse':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="42.039604,9.012893,km")
           
        elif self.region == 'Franche-Comte':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="47.134321,6.022302,km")

        elif self.region == 'Haute Normandie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="49.524641,0.882833,km")

        elif self.region == 'Ile-de-France':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="48.84992,2.637041,km")
           
        elif self.region == 'Languedoc-Roussillon':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="43.591236,3.258363,km")

        elif self.region == 'Limousin':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="45.893223,1.569602,km")

        elif self.region == 'Lorraine':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="48.874423,6.208093,km")

        elif self.region == 'Midi-Pyrenees':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="44.085943,1.520862,km")

        elif self.region == 'Nord-Pas-de-Calais':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="50.573277,2.324468,km")

        elif self.region == 'Pays de la Loire':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="47.763284,-0.329969,km")
           
        elif self.region == 'Picardie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="49.663613,2.528073,km")

        elif self.region == 'Poitou-Charentes':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="45.903552,-0.309184,km")
           
        elif self.region == "Provence-Alpes-Cote-d'Azur":
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="43.935169,6.067919,km")

        elif self.region == 'Rhone-Alpes':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="45.16958,5.450282,km")

        elif self.region == 'Guadeloupe':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="16.265,-61.551,km")

        elif self.region == 'Martinique':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="14.641528,-61.024174,km")

        elif self.region == 'Guyane':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="3.933889,-53.125782,km")

        elif self.region == 'La Reunion':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="-21.115141,55.536384,km")

        elif self.region == 'Mayotte':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           since='2018-01-1',geocode="-12.8275,45.166244,km")

        
        return self.newTweets

    def displayTweetsByRegion(self):

        for tweet in self.newTweets:
            print(tweet.text)
            print("Region....")
            print(self.region)
        

    def initializeAPI(self):
        # Authentication and access using keys
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Return API with authentication
        api = tweepy.API(auth)
        return api


tweet = TweetByRegion("Nord-Pas-de-Calais","#JO2018")
tweet.retrieveTweets()
tweet.displayTweetsByRegion()