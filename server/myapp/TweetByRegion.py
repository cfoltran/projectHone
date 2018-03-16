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
#https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder?hl=fr
    def retrieveTweets(self): 
        # API Authentification
        api = self.initializeAPI()
       
        if self.region == 'France':
           self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           granularity="country", place_id="ChIJMVd4MymgVA0R99lHx5Y__Ws")
          
        elif self.region == 'Alsace':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJv5Z326NGkUcR4CQ3mrlfCgE")
        
        elif self.region == 'Aquitaine':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city", place_id="ChIJXUV5MymgVA0RCYiUCcIMmcI")
        
        elif self.region == 'Auvergne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city", place_id="ChIJ3Y9LbrHk9kcRUCTjy688CQE")
            
        elif self.region == 'Basse Normandie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJu46ajCY6CkgRICW1T0gUDAE")
            
        elif self.region == 'Bourgogne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJt9nzCDkE8kcRECUNszTOCQE")
        
        elif self.region == 'Bretagne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJr45-rmHKEUgRsCTfNs2lDAE")
           
        elif self.region == 'Centre':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city", place_id="ChIJiV0INnu55EcRMCUzBdfIDQE")


        
        elif self.region == 'Champagne-Ardenne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city", place_id="ChIJXad-Rv906UcRPauSZXj2v5o")
           
        elif self.region == 'Corse':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJcQmbsAMk1xIRjcuhcewihag")
           
        elif self.region == 'Franche-Comte':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJJwKvjhhjjUcREV-uvEkQBec")

        elif self.region == 'Haute Normandie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJfYshlSMv4EcRRVdFNfaAXnA")

        elif self.region == 'Ile-de-France':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJF4ymA8Th5UcRcCWLaMOCCwE")
           
        elif self.region == 'Languedoc-Roussillon':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJWcV6wLBksRIRQCRlFiGIBwE")

        elif self.region == 'Limousin':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJ9Qt-IC4Q-UcRbgZJ0DHNvJI")

        elif self.region == 'Lorraine':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJ1ZAR_lOXlEcR8CQ3mrlfCgE")

        elif self.region == 'Midi-Pyrenees':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJi5Fh1PkgrBIRgCQ7L5z2BgE")

        elif self.region == 'Nord-Pas-de-Calais':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJCfJtqIjVwkcR7-qpwxdEZek")

        elif self.region == 'Pays de la Loire':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           granularity="city",place_id="ChIJQQUJqjgXBUgRtkcc2Asrls8")
           
        elif self.region == 'Picardie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJL9Lah0CE50cRbrAvKEy_vg0")

        elif self.region == 'Poitou-Charentes':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJbRILoIqxAEgRoCTnYJLTBQE")
           
        elif self.region == "Provence-Alpes-Cote-d'Azur":
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            granularity="city",place_id="ChIJrVP5ihlothIRp9EWPSaQFrc")

        elif self.region == 'Rhone-Alpes':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            granularity="city",place_id="ChIJS_HI7dPZikcRua8Cids1k3c")

        elif self.region == 'Guadeloupe':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            granularity="city",place_id="ChIJUX0od1p1DowRqwdKtzc-vuw")

        elif self.region == 'Martinique':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
           granularity="city",place_id="ChIJDQdmAPmgaowRsOevFxIbAOE")

        elif self.region == 'Guyane':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            granularity="city",place_id="ChIJU9f3hVcVEo0RRvQKD-n3J94")

        elif self.region == 'La Reunion':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            granularity="city",place_id="ChIJO-S4EIF3eCER-erb7ImOf0o")

        elif self.region == 'Mayotte':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
           granularity="city",place_id="ChIJu43y3DMOCiIRSyr-lWcXMv8")

        
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
print(tweet.retrieveTweets())
#tweet.displayTweetsByRegion()