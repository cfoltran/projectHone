import tweepy
import json
import datetime
import pandas
import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from Credentials import *


MARGIN_DAY = 1  # Value used to retrieve all tweets below it
MAX_TWEETS = 4
TWEETS_PER_SEARCH = 2 # Max Value = 100


class Statistics:
    def __init__(self, hashtagSearched):
        self.hashtag = "#" + hashtagSearched

    def retrieveStatistics(self):
        # API Authentification
        api = self.initializeAPI()
        # Get today date
        today = datetime.date.today()
        # Create the margin
        margin = datetime.timedelta(days=MARGIN_DAY)

        ## Loop to get more tweets (>100)
        # oldestTweetId store the oldest tweet id
        oldestTweetId = None
        # tweetCount store the number of tweets retrieved
        tweetCount = 0
        # Store tweets with their informations
        dataTweets = pandas.DataFrame(columns=['Content','Date','Retweets','Likes'])

        while tweetCount < MAX_TWEETS:
            # First iteration, we retrieve the most recent tweets
            if(not oldestTweetId):
                newTweets = api.search(q=self.hashtag, since=today-margin, lang="fr", count=TWEETS_PER_SEARCH)
            else:
                newTweets = api.search(q=self.hashtag, since=today-margin, lang="fr", count=TWEETS_PER_SEARCH, max_id=oldestTweetId-1)
            # If there is no more tweets found we exit the while loop
            if not newTweets:
                print("No more tweets with this hashtag ! \n")
                break
            else:    
                # Keep the oldest tweet id to retrieve older tweets (used as the maximum id to reach)
                oldestTweetId = newTweets[len(newTweets)-1].id

                # Add informations about new tweets in dataTweets
                data = pandas.DataFrame(columns=['Content','Date','Retweets','Likes'])
                data['Content'] = np.array([tweet.text for tweet in newTweets])
                data['Date'] = np.array([tweet.created_at for tweet in newTweets])
                data['Retweets'] = np.array([tweet.retweet_count for tweet in newTweets])
                data['Likes'] = np.array([tweet.favorite_count for tweet in newTweets])
                dataTweets = dataTweets.append(data)

                # Increment number of tweets
                tweetCount += len(newTweets)
        ##
        print("Number of tweets : {}.\n".format(tweetCount))
        # Sort dataTweets and drop duplicates (Sort by retweets)
        dataTweets = dataTweets.sort_values(by='Retweets', ascending=False).drop_duplicates(subset='Content')
        print(dataTweets)

    def initializeAPI(self):
        # Authentication and access using keys
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Return API with authentication
        api = tweepy.API(auth)
        return api


stats = Statistics("MHSCOL")
stats.retrieveStatistics()