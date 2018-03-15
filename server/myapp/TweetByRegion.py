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
           geocode="46.227638,2.213749,km", granularity="country")
          
        elif self.region == 'Alsace':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.31818,7.441624,km", granularity="city")
        
        elif self.region == 'Aquitaine':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="44.700222,-0.299579,km", granularity="city")
        
        elif self.region == 'Auvergne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="45.70327,3.344854,km", granularity="city")
            
        elif self.region == 'Basse Normandie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.878847,-0.515749,km", granularity="city")
            
        elif self.region == 'Bourgogne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="47.052505,4.383721,km", granularity="city")
        
        elif self.region == 'Bretagne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.202047,-2.932644,km", granularity="city")
           
        elif self.region == 'Centre':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="47.751569,1.675063,km", granularity="city")
        
        elif self.region == 'Champagne-Ardenne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.793409,4.472525,km", granularity="city")
           
        elif self.region == 'Corse':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="42.039604,9.012893,km", granularity="city")
           
        elif self.region == 'Franche-Comte':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="47.134321,6.022302,km", granularity="city")

        elif self.region == 'Haute Normandie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="49.524641,0.882833,km", granularity="city")

        elif self.region == 'Ile-de-France':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.84992,2.637041,km", granularity="city")
           
        elif self.region == 'Languedoc-Roussillon':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="43.591236,3.258363,km", granularity="city")

        elif self.region == 'Limousin':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="45.893223,1.569602,km", granularity="city")

        elif self.region == 'Lorraine':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.874423,6.208093,km", granularity="city")

        elif self.region == 'Midi-Pyrenees':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="44.085943,1.520862,km", granularity="city")

        elif self.region == 'Nord-Pas-de-Calais':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="50.573277,2.324468,km", granularity="city")

        elif self.region == 'Pays de la Loire':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="47.763284,-0.329969,km", granularity="city")
           
        elif self.region == 'Picardie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="49.663613,2.528073,km", granularity="city")

        elif self.region == 'Poitou-Charentes':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="45.903552,-0.309184,km", granularity="city")
           
        elif self.region == "Provence-Alpes-Cote-d'Azur":
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            geocode="43.935169,6.067919,km", granularity="city")

        elif self.region == 'Rhone-Alpes':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="45.16958,5.450282,km", granularity="city")

        elif self.region == 'Guadeloupe':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            geocode="16.265,-61.551,km", granularity="city")

        elif self.region == 'Martinique':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            geocode="14.641528,-61.024174,km", granularity="city")

        elif self.region == 'Guyane':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            geocode="3.933889,-53.125782,km", granularity="city")

        elif self.region == 'La Reunion':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            geocode="-21.115141,55.536384,km", granularity="city")

        elif self.region == 'Mayotte':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            geocode="-12.8275,45.166244,km", granularity="city")

        
        return self.newTweets



    def displayTweetsByRegion(self):# for testing the class

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


tweet = TweetByRegion("Guyane","#JO2018")
tweet.retrieveTweets()
tweet.displayTweetsByRegion()