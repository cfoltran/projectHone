import tweepy
import json
import datetime
import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from Connect import Connect

MARGIN_DAY = 1  # Value used to retrieve all tweets below it

TWEETS_PER_SEARCH = 100 # Max Value = 100
#https://developer.twitter.com/en/docs/geo/places-near-location/self.api-reference/get-geo-search
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
        #today = datetime.date.today()
        # Create the margin
        #margin = datetime.timedelta(days=MARGIN_DAY)

        if self.region == 'France':
            self.newTweets = self.api.search(q="*", lang="fr", count=TWEETS_PER_SEARCH)
          
        elif self.region == 'Alsace':
            place_id = "92ec8ea0ba8ffff1"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'Aquitaine':
            place_id = "8e73e1421b45f5e8"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Auvergne':
            place_id = "b2652102823ca640"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Basse_Normandie':
            place_id = "b9c33633c20ad451"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Bourgogne':
            place_id = "60c859887b142d5f"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Bretagne':
            place_id = "57e5628aab63276b"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Centre':
            place_id = "807d76bc84f359c7"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Champagne-Ardenne':
            place_id = "8e0da10618d1836b"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Corse':
            place_id = "0e63aaa08b0593a4"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Franche-Comte':
            place_id = "3ea75b7392b74cae"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Haute_Normandie':
            place_id = "8e0b6cfe16a8e576"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Ile-de-France':
            place_id = "f9c4cad0af2337fa"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
           
        elif self.region == 'Languedoc-Roussillon':
            place_id = "8aee614456e63150"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'Limousin':
            place_id = "f54315bcf7afaafe"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Lorraine':
            place_id = "2ed84dd278f9028f"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Midi-Pyrenees':
            place_id = "829cf2c4a7c5251d"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Nord-Pas-de-Calais':
            place_id = "df9cb72656eba326"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
          
        elif self.region == 'Pays_de_la_Loire':
            place_id = "9dc3b9da3afde6a8"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Picardie':
            place_id = "c7433f8be99a2328"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
        
        elif self.region == 'Poitou-Charentes':
            place_id = "1ce67713116497af"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)
    
        elif self.region == "Provence-Alpes-Cote-d_Azur":
            place_id = "3da6b5ad7b0af478"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'Rhone-Alpes':
            place_id = "771dd147cda1a16a"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'Guadeloupe':
            place_id = "4e9baf84e2232342"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'Martinique':
            place_id = "15bddd8209796b5e"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'Guyane':
            place_id = "991b4344edc2d520"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'La_Reunion':
            place_id = "0ab9fd6675769ba4"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.region == 'Mayotte':
            place_id = "2e1db4ccd414851e"
            self.newTweets = self.api.search(q="place:%s" % place_id, lang="fr", count=TWEETS_PER_SEARCH)



        return self.newTweets

    def initializeAPI(self):
        co = Connect()
        return co.authentification()
            