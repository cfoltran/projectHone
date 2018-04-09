import tweepy
import json
import datetime
import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from Connect import Connect
from DataTweet import DataTweet
import json



REGIONS = {
    "Ile-de-France" : "f9c4cad0af2337fa",
    "Auvergne-Rhone-Alpes" : "b2652102823ca640",
    "Bourgogne-Franche-Comte" : "60c859887b142d5f",
    "Bretagne" : "57e5628aab63276b",
    "Centre-Val_de_Loire" : "3f5897b87d2bf56c",
    "Corse" : "0e63aaa08b0593a4",
    "Grand_Est" : "590d65437809f135",
    "Hauts-de-France" : "fec0a87de4183158",
    "Normandie" : "8e0b6cfe16a8e576",
    "Nouvelle-Aquitaine" : "2f4cc128bb4fb146",
    "Occitanie" : "829cf2c4a7c5251d",
    "Pays_de_la_Loire" : "9dc3b9da3afde6a8",
    "Provence-Alpes-Cote_dAzur" : "3da6b5ad7b0af478",
    "La_Reunion" : "0ab9fd6675769ba4",
    "Martinique" : "15bddd8209796b5e",
    "Guyane" : "991b4344edc2d520",
    "Guadeloupe" : "4e9baf84e2232342",
    "Mayotte" : "2e1db4ccd414851e"
}

MARGIN_DAY = 100  # Value used to retrieve all tweets below it

TWEETS_PER_SEARCH = 1 # Max Value = 100

class TweetByRegion:
   
    region = ""
    hashtag = "#"
    newTweets = ""
    def __init__(self, regionSearched,hashtagSearched):
        self.region = regionSearched
        
        self.hashtag = hashtagSearched

        
        # self.API Authentification
        self.api = self.initializeAPI()




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
            print("-----------------------------date-----------------------------------------")
            print(tweet.created_at)
            print("-----------------------------Emetteur-----------------------------------------")
            print(tweet.user.name)
            print("---------------------------------place------------------------------")
            print(tweet.place.name)
          
          
        #date : tweet.created_at
        #tweet.user.location : localisation
        #tweet.user.name : nom de l'utilisateur

    def initializeAPI(self):
       co = Connect()
       co.authentification()
       return co.authentification()


tweet = TweetByRegion("IDF","bonjour")
tweet.retrieveTweets()
tweet.displayTweetsByRegion()
