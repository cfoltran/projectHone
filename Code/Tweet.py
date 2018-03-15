#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textblob import Blobber
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import json
import carmen
import tweepy
class Tweet:
    text = ""
    sender = "inconnu"
    dateTweet = ""
    nbLike = 0
    nbRT = 0
    region = "inconnu"
    sentiment = ""
    #consumer_key = 'd9UUsBFWzdBrMv8HwEay8mzeP'
	#consumer_secret = 'YhheggCydfUm3VwHiT14ig1lM0ahLAIaFbtBfq71JgWp6dHA5B'
	#access_token = '960451934535774208-g3s0XuB7efDic5lQBK8RNfSa4GL5GKB'
	#access_token_secret = 'XW05i2CvXt2Th9ipoY8wU4ICk39mVhSI051DPj7ad8gej'

    def __init__(self, text, sender, date, region):
        self.text = text
        self.sender = sender
        self.dateTweet = date 
        self.region = region
        



    def getText(self):
        return self.text

    def getSender(self):
        return self.sender

    def getDateTweet(self):
        return self.dateTweet

    def getnbLike(self):
        return self.nbLike

    def getnbRT(self):
        return self.nbRT

    def getRegion(self):
        return self.region

    def getSentiment(self):
        return self.sentiment


    def setRegion(self,region):
        self.region = region

    def setText(self,text):
         self.text = text

    def setSender(self,sender):
         self.sender = sender

    def setDateTweet(self,date):
         self.dateTweet = date

    def setNbLike(self,nbLike):
        this.nbLike = nbLike

    def setNbRT(self,nbRT):
        this.nbRT = nbRT

    def incrementnbLike(self):
         self.nbLike += 1 

    def incrementnbRT(self):
         self.nbRT += 1

    
    def displayTweet(self):
        print(self.sender)
        print(self.text)
        print(self.dateTweet)

    #initialize and return sentiment
    def analyze_text(self):
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        blob = tb(self.text)
        self.sentiment = blob.sentiment
        return self.sentiment # polarité et subjectivité

    #initialize and return sentiment version 2 (polarité)
    def analyze_textV2(self):
        french_blob = TextBlob(self.text)
        english_blob = french_blob.translate(from_lang="fr",to='en')
        self.sentiment = english_blob.sentiment.polarity #récupère la polarité seulement
        return self.sentiment



    # methode pour mettre le tweet dans la conformite du fichier json
    def serialize(self):
        return {
            'text': self.text,
            'sender': self.sender,
            'region': json.loads(json.dumps(self.region.tolist())),
            'dateTweet': self.dateTweet,
            'nbLike': self.nbLike,
            'nbRT': self.nbRT,
            'sentiment': json.loads(json.dumps(self.sentiment))
        }

    def tweetsParRegion(self, region):
        #consumer_key = 'd9UUsBFWzdBrMv8HwEay8mzeP'
	    #consumer_secret = 'YhheggCydfUm3VwHiT14ig1lM0ahLAIaFbtBfq71JgWp6dHA5B'
	    #access_token = '960451934535774208-g3s0XuB7efDic5lQBK8RNfSa4GL5GKB'
	    #access_token_secret = 'XW05i2CvXt2Th9ipoY8wU4ICk39mVhSI051DPj7ad8gej'
        auth = tweepy.OAuthHandler('d9UUsBFWzdBrMv8HwEay8mzeP', 'YhheggCydfUm3VwHiT14ig1lM0ahLAIaFbtBfq71JgWp6dHA5B')
        auth.set_access_token('960451934535774208-g3s0XuB7efDic5lQBK8RNfSa4GL5GKB', 'XW05i2CvXt2Th9ipoY8wU4ICk39mVhSI051DPj7ad8gej')
        
        api = tweepy.API(auth)
        places = api.geo_search(query=region, granularity="country")
        place_id = places[0].id
        tweets = api.search(q="place:%s" % place_id)
        return tweets




    


