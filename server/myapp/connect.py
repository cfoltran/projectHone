#Class to connect to the Twitter API
#I don't know if it's a good idea, neither if it's working because I didn't had time yet to
#set up the docker to test it.

import tweepy
import json
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

class Connect :
	consumer_key = ""
	consumer_secret = ""
	access_token = ""
	access_token_secret = ""
	auth = 0
	api = 0
	
	def __init__():
	self.consumer_key = 'd9UUsBFWzdBrMv8HwEay8mzeP'
	self.consumer_secret = 'YhheggCydfUm3VwHiT14ig1lM0ahLAIaFbtBfq71JgWp6dHA5B'
	self.access_token = '960451934535774208-g3s0XuB7efDic5lQBK8RNfSa4GL5GKB'
	self.access_token_secret = 'XW05i2CvXt2Th9ipoY8wU4ICk39mVhSI051DPj7ad8gej'
	self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
	self.api = tweepy.API(auth, wait_on_rate_limit = True)
	
	def authentication() :
		self.auth.set_access_token(access_token, access_token_secret)