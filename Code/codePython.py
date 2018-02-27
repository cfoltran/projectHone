"""import tweepy
from textblob import TextBlob

consumer_key = 'd9UUsBFWzdBrMv8HwEay8mzeP'
consumer_secret = 'YhheggCydfUm3VwHiT14ig1lM0ahLAIaFbtBfq71JgWp6dHA5B'

access_token = '960451934535774208-g3s0XuB7efDic5lQBK8RNfSa4GL5GKB'
access_token_secret = 'XW05i2CvXt2Th9ipoY8wU4ICk39mVhSI051DPj7ad8gej'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

#public_tweets = api.search('snowboard')

#for tweet in public_tweets:
#	print(tweet.text)
#	analysis = TextBlob(tweet.text)
#	print(analysis.sentiment)

for tweet in tweepy.Cursor(api.search, q="#OlympicGames2018",count=100,
		lang="en", since="2018-01-01").items():
	print(tweet.created_at, tweet.text)
	print(TextBlob(tweet.text).sentiment.polarity)

"""
#           Partie ANGLAISE
"""
import tweepy
from textblob import TextBlob

consumer_key = 'd9UUsBFWzdBrMv8HwEay8mzeP'
consumer_secret = 'YhheggCydfUm3VwHiT14ig1lM0ahLAIaFbtBfq71JgWp6dHA5B'

access_token = '960451934535774208-g3s0XuB7efDic5lQBK8RNfSa4GL5GKB'
access_token_secret = 'XW05i2CvXt2Th9ipoY8wU4ICk39mVhSI051DPj7ad8gej'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

for tweet in tweepy.Cursor(api.search, q="#OlympicGames2018",count=100,
		lang="en", since="2018-01-01").items():
	print(tweet.created_at, tweet.text)
	print(TextBlob(tweet.text).sentiment.polarity)
	
"""

#           Partie FRANCAISE

import tweepy
import json
#import six
#from flask import Flask, jsonify, abort, request, make_response, url_for
#from flask_cors import CORS, cross_origin
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

consumer_key = 'd9UUsBFWzdBrMv8HwEay8mzeP'
consumer_secret = 'YhheggCydfUm3VwHiT14ig1lM0ahLAIaFbtBfq71JgWp6dHA5B'

access_token = '960451934535774208-g3s0XuB7efDic5lQBK8RNfSa4GL5GKB'
access_token_secret = 'XW05i2CvXt2Th9ipoY8wU4ICk39mVhSI051DPj7ad8gej'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

def polarityName(tweet):
		file = tweet.author._json
		decodedfile = json.dumps(file)
		decodedfile = json.loads(decodedfile)
		name = str(decodedfile['screen_name'])
		polarity = tb(tweet.text).sentiment
		return name, polarity
	
def locat(tweet):
		fileLocation = tweet.author._json
		decodeFileLocation = json.dumps(fileLocation)
		decodeFileLocation = json.loads(decodeFileLocation)
		loca = str(decodeFileLocation['Location'])
		return loca
		
for tweet in tweepy.Cursor(api.search, q="#jeuxolympiques2018",count=25,
	lang="fr", since="2018-02-021").items():
	#print(tweet.created_at, tweet.text) #print the global twitter
	#print(tb(tweet.text).sentiment) #print a number who juge the positiveness
	#print(tweet.created_at) #print the date of the tweet
	#print(tweet.location)
	
	#print(Location(tweet))	
	break
	file = tweet.author._json #
	decodedfile = json.dumps(file) #               Return the name
	decodedfile = json.loads(decodedfile) #
	print(polarityName(tweet)) #
	
	print(loca(tweet))