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
            place_id = "ChIJMVd4MymgVA0R99lHx5Y__Ws"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
          
        elif self.region == 'HAUTSDEFRANCE':
            place_id = "fec0a87de4183158"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'GRANDEST':
            place_id = " 590d65437809f135"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'BOURGOGNEFRANCHECOMTE':
            place_id = "60c859887b142d5f"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
            
        elif self.region == 'AUVERGNERHONEALPES':
            place_id = "b2652102823ca640"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'PROVENCEALPESCOTEDASUR':
            place_id = "3da6b5ad7b0af478"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
           
        elif self.region == 'OCCITANIE':
            place_id = "829cf2c4a7c5251d"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)


        
        elif self.region == 'AQUITAINE':
            place_id = "2f4cc128bb4fb146"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
           
        elif self.region == 'PAYSDELALOIRE':
            place_id = "9dc3b9da3afde6a8"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
           
        elif self.region == 'BRETAGNE':
            place_id = "57e5628aab63276b"
            self.newTweets = api.search(q=self.hashtag + "&place=%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'NORMANDIE':
            place_id = "8e0b6cfe16a8e576"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

           
        elif self.region == 'IDF':
            place_id = "f9c4cad0af2337fa"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)


        elif self.region == 'CENTREVALDELOIRE':
            place_id = "3f5897b87d2bf56c"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'CORSE':
            place_id = "0e63aaa08b0593a4"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'GUYANE':
            place_id = "991b4344edc2d520"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'MARTINIQUE':
            place_id = "15bddd8209796b5e"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'MAYOTTE':
            place_id = "2e1db4ccd414851e"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'LAREUNION':
            place_id = "0ab9fd6675769ba4"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'GUADELOUPE':
            place_id = "4e9baf84e2232342"
            self.newTweets = api.search(q=self.hashtag + "&place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        

        

        
        return self.newTweets # return data on tweets by a region, retrieve these data in json.

    def displayTweetsByRegion(self):# for testing the class
        

        for tweet in self.newTweets:
            print(tweet.text)
            print("----------------------------------------------------------------------")
          
        

    def initializeAPI(self):
        # Authentication and access using keys
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Return API with authentication
        api = tweepy.API(auth)
        return api


tweet = TweetByRegion("BRETAGNE","bretagne")
tweet.retrieveTweets()
tweet.displayTweetsByRegion()