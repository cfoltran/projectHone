import tweepy
import json
import datetime
#ihhh
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

       
       
        if self.region == 'FRANCE':
           self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
           geocode="46.227638,2.213749,700km",since=today-margin)
          
        elif self.region == 'HAUTSDEFRANCE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="50.287134,2.781225,130km",since=today-margin)
            #place_id="ChIJv5Z326NGkUcR4CQ3mrlfCgE"
        
        elif self.region == 'GRANDEST':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.699803,6.187807,160km",since=today-margin)
        
        elif self.region == 'FRANCHECOMTE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="47.134321,6.022302,120km",since=today-margin)
            
        elif self.region == 'AUVERGNE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="45.70327,3.344854,150km",since=today-margin)
            
        
        elif self.region == 'PROVENCE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="44.014494,6.211644,120km",since=today-margin)
           
        elif self.region == 'OCCITANIE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="43.892723,3.282762,150km",since=today-margin)


        
        elif self.region == 'AQUITAINE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="44.700222,-0.299579,160km",since=today-margin)
           
        elif self.region == 'PAYSDELALOIRE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="44.700222,-0.299579,160km",since=today-margin)
           
        elif self.region == 'BRETAGNE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.202047,-2.932644,130km",since=today-margin)

        elif self.region == 'NORMANDIE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.87987,0.171253,120km",since=today-margin)

           
        elif self.region == 'IDF':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="48.84992,2.637041,80km",since=today-margin)

        elif self.region == 'VALDELOIRE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="47.55324,1.010529,75km",since=today-margin)

        elif self.region == 'CORSE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="42.039604,9.012893,110km",since=today-margin)

        elif self.region == 'GUYANE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="3.933889,-53.125782,150km",since=today-margin)

        elif self.region == 'MARTINIQUE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="14.641528,-61.024174,25km",since=today-margin)

        elif self.region == 'MAYOTTE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="-12.8275000,45.1662440,18km",since=today-margin)

        elif self.region == 'LAREUNION':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="-21.115141,55.536384,30km",since=today-margin)

        elif self.region == 'GUADELOUPE':
            self.newTweets = api.search(q=self.hashtag, lang="fr", count=TWEETS_PER_SEARCH, 
            geocode="16.265,-61.551,70km",since=today-margin)

        

        

        
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


tweet = TweetByRegion("NORMANDIE","#JO2018")
tweet.retrieveTweets()
tweet.displayTweetsByRegion()