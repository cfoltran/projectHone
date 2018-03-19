import tweepy
import json
import datetime

import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from Credentials import *

MARGIN_DAY = 1  # Value used to retrieve all tweets below it

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
        # Get today date
        today = datetime.date.today()
        # Create the margin
        margin = datetime.timedelta(days=MARGIN_DAY)

        # API Authentification
        api = self.initializeAPI()
       
        if self.region == 'France':
           self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           granularity="country", place_id="ChIJMVd4MymgVA0R99lHx5Y__Ws",since=today-margin)
          
        elif self.region == 'Alsace':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJv5Z326NGkUcR4CQ3mrlfCgE",since=today-margin)
        
        elif self.region == 'Aquitaine':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJXUV5MymgVA0RCYiUCcIMmcI",since=today-margin)
        
        elif self.region == 'Auvergne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJ3Y9LbrHk9kcRUCTjy688CQE",since=today-margin)
            
        elif self.region == 'Basse Normandie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJu46ajCY6CkgRICW1T0gUDAE",since=today-margin)
            
        elif self.region == 'Bourgogne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJt9nzCDkE8kcRECUNszTOCQE",since=today-margin)
        
        elif self.region == 'Bretagne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJr45-rmHKEUgRsCTfNs2lDAE",since=today-margin)
           
        elif self.region == 'Centre':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJiV0INnu55EcRMCUzBdfIDQE",since=today-margin)


        
        elif self.region == 'Champagne-Ardenne':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJXad-Rv906UcRPauSZXj2v5o",since=today-margin)
           
        elif self.region == 'Corse':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJcQmbsAMk1xIRjcuhcewihag",since=today-margin)
           
        elif self.region == 'Franche-Comte':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJJwKvjhhjjUcREV-uvEkQBec",since=today-margin)

        elif self.region == 'Haute Normandie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJfYshlSMv4EcRRVdFNfaAXnA",since=today-margin)

        elif self.region == 'Ile-de-France':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJF4ymA8Th5UcRcCWLaMOCCwE",since=today-margin)
           
        elif self.region == 'Languedoc-Roussillon':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJWcV6wLBksRIRQCRlFiGIBwE",since=today-margin)

        elif self.region == 'Limousin':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJ9Qt-IC4Q-UcRbgZJ0DHNvJI",since=today-margin)

        elif self.region == 'Lorraine':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJ1ZAR_lOXlEcR8CQ3mrlfCgE",since=today-margin)

        elif self.region == 'Midi-Pyrenees':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJi5Fh1PkgrBIRgCQ7L5z2BgE",since=today-margin)

        elif self.region == 'Nord-Pas-de-Calais':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJCfJtqIjVwkcR7-qpwxdEZek",since=today-margin)

        elif self.region == 'Pays de la Loire':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJQQUJqjgXBUgRtkcc2Asrls8",since=today-margin)
           
        elif self.region == 'Picardie':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJL9Lah0CE50cRbrAvKEy_vg0",since=today-margin)

        elif self.region == 'Poitou-Charentes':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJbRILoIqxAEgRoCTnYJLTBQE",since=today-margin)
           
        elif self.region == "Provence-Alpes-Cote-d'Azur":
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            place_id="ChIJrVP5ihlothIRp9EWPSaQFrc",since=today-margin)

        elif self.region == 'Rhone-Alpes':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            place_id="ChIJS_HI7dPZikcRua8Cids1k3c",since=today-margin)

        elif self.region == 'Guadeloupe':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            place_id="ChIJUX0od1p1DowRqwdKtzc-vuw",since=today-margin)

        elif self.region == 'Martinique':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            place_id="ChIJDQdmAPmgaowRsOevFxIbAOE",since=today-margin)

        elif self.region == 'Guyane':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            place_id="ChIJU9f3hVcVEo0RRvQKD-n3J94",since=today-margin)

        elif self.region == 'La Reunion':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            place_id="ChIJO-S4EIF3eCER-erb7ImOf0o",since=today-margin)

        elif self.region == 'Mayotte':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH,
            place_id="ChIJu43y3DMOCiIRSyr-lWcXMv8",since=today-margin)

        
        return self.newTweets # return data on tweets by a region, retrieve these data in json.



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


#tweet = TweetByRegion("France","#JO2018")
#print(tweet.retrieveTweets())
#tweet.displayTweetsByRegion()