
# -*- coding: utf-8 -*-
#!/usr/bin/env python

#import the class Tweet
from Tweet import *
import tweepy
import json
untweet = Tweet("Cette voiture est moche", "alexandre","2018-02-27","Bretagne")
untweet.displayTweet()
print("Sentiment...")
print(untweet.analyze_textV2())
print("Location...")

print(untweet.region)

print(tweetsParRegion("Bretagne"))