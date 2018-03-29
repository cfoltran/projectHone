import tweepy
import datetime
import pandas
import numpy as np
from SentimentAnalyze import Sentiment
from Connect import Connect
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

textblob = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

MARGIN_DAY = 1  # Value used to retrieve all tweets below it
MAX_TWEETS = 500
TWEETS_PER_SEARCH = 100  # Max Value = 100


class StatisticsByHashtag:
    def __init__(self, hashtagSearched):
        self.hashtag = "#" + str(hashtagSearched)
        self.api = self.initializeAPI()


    def retrieveStatistics(self):
        # API Authentification
        # Get today date
        today = datetime.date.today()

        print(today)
        # Create the margin
        margin = datetime.timedelta(days=MARGIN_DAY)

        ## Loop to get more tweets (>100)
        # oldestTweetId store the oldest tweet id
        oldestTweetId = None
        # tweetCount store the number of tweets retrieved
        tweetCount = 0

        if self.hashtag != None:
            # Store tweets with their informations
            dataTweets = pandas.DataFrame(columns=['Content','Date','Retweets','Likes'])

            while tweetCount < MAX_TWEETS:
                # First iteration, we retrieve the most recent tweets
                if(not oldestTweetId):
                    newTweets = self.api.search(q=self.hashtag, since=today-margin, lang="fr", count=TWEETS_PER_SEARCH)
                else:
                    newTweets = self.api.search(q=self.hashtag, since=today-margin, lang="fr", count=TWEETS_PER_SEARCH, max_id=oldestTweetId-1)
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
                    data['Polarity'] = np.array([self.getPolarity(tweet.text) for tweet in newTweets])
                    dataTweets = dataTweets.append(data)

                    # Increment number of tweets
                    tweetCount += len(newTweets)

            # Sort dataTweets and drop duplicates
            dataTweets = dataTweets.sort_values(by='Retweets', ascending=False).drop_duplicates(subset='Content')
            # Reset index to allow the serialization
            dataTweets.reset_index(inplace=True, drop=True)


            # Creation of stats
            totalPolarity = 0.0
            totalRT = 0
            nbTweets = 0

            for tweet in dataTweets.iterrows():
                nbTweets += 1
                totalRT += tweet[1]['Retweets']
                totalPolarity += tweet[1]['Polarity']

            data = pandas.DataFrame()
            if nbTweets != 0:
                data['AverageRetweets'] = np.array([totalRT / nbTweets])
                data['AveragePolarity'] = np.array([totalPolarity / nbTweets])
            else:
                data['AverageRetweets'] = np.array([0])
                data['AveragePolarity'] = np.array([0])
            data['NumbersOfTweets'] = np.array([nbTweets])

            return data

    def getPolarity(self, tweet):
        pol = textblob(tweet).sentiment
        return pol[0]


    def initializeAPI(self):
        co = Connect()
        return co.authentification()
