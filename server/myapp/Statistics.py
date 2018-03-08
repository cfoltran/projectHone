import tweepy
import json
import datetime
import pandas
import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from Credentials import *


MARGIN_DAY = 1  # Value used to retrieve all tweets below it
MAX_TWEETS = 10
TWEETS_PER_SEARCH = 5 # Max Value = 100

regions = {
    32 : "50.287134,2.781225,130km", #HAUTSDEFRANCE
    44 : "48.699803,6.187807,160km", #GRANDEST
    27 : "47.134321,6.022302,120km", #FRANCHECOMTE
    84 : "45.70327,3.344854,150km", #AUVERGNE
    93 : "44.014494,6.211644,120km", #PROVENCE
    76 : "43.892723,3.282762,150km", #OCCITANIE
    75 : "44.700222,-0.299579,160km", #AQUITAINE
    52 : "44.700222,-0.299579,160km", #LOIRE
    53 : "48.202047,-2.932644,130km", #BRETAGNE
    28 : "48.87987,0.171253,120km", #NORMANDIE
    11 : "48.84992,2.637041,80km", #IDF
    24 : "47.55324,1.010529,75km", #VALDELOIRE
    94 : "42.039604,9.012893,110km" #CORSE
}


class Statistics:
    def __init__(self, hashtagSearched=None, region=None):
        self.hashtag = "#" + str(hashtagSearched)
        self.region = region

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

        if self.region == None and self.hashtag != None:
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
                    
            # Sort dataTweets and drop duplicates (Sort by retweets)
            dataTweets = dataTweets.sort_values(by='Retweets', ascending=False).drop_duplicates(subset='Content')
            # Reset index to allow the serialization
            dataTweets.reset_index(inplace=True, drop=True)
            # Serialize the dataFrame to a json & return it
            return dataTweets.to_json(orient='index')

        else:
            # Store tweets with their informations
            dataTweets = pandas.DataFrame(columns=['Content','Date','Retweets','Likes'])

            while tweetCount < MAX_TWEETS:
                # First iteration, we retrieve the most recent tweets
                if(not oldestTweetId):
                    newTweets = api.search(q="*", since=today-margin, lang="fr", geocode=regions.get(int(self.region)), count=TWEETS_PER_SEARCH)
                else:
                    newTweets = api.search(q="*", since=today-margin, lang="fr", geocode=regions.get(int(self.region)), count=TWEETS_PER_SEARCH, max_id=oldestTweetId-1)
                # If there is no more tweets found we exit the while loop
                if not newTweets:
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
                    
            # Sort dataTweets and drop duplicates (Sort by retweets)
            dataTweets = dataTweets.sort_values(by='Retweets', ascending=False).drop_duplicates(subset='Content')
            # Reset index to allow the serialization
            dataTweets.reset_index(inplace=True, drop=True)
            # Serialize the dataFrame to a json & return it
            return dataTweets.to_json(orient='index')

    def initializeAPI(self):
        # Authentication and access using keys
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        # Return API with authentication
        api = tweepy.API(auth)
        return api