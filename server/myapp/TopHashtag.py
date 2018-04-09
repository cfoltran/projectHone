import tweepy
import json
import datetime
from Connect import Connect

class TopHashtag:
    def __init__(self):
        self.tweethashtag = ''
        self.hashtags={"#jeuxolympiques2018" :0 , "#JO2018" :0 , "#JO" :0 , "#espritbleu" :0 , "#pyeongchang2018" :0}
        self.api = self.initializeAPI()

    def defaultSearch(self):

        today = datetime.date.today()

        for hashtag in self.hashtags:
            cpt = 0
            self.tweethashtag = self.api.search(q=hashtag, count = 5, lang="fr", start_time=str(today) + "T00:00:00Z", end_time=str(today) + "T01:00:00Z")
            for tweet in self.tweethashtag:
                cpt = cpt + 1
            self.hashtags[hashtag] = cpt
            return self.hashtags



    def initializeAPI(self):
        co = Connect()
        return co.authentification()
