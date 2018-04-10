import json
TWEETS_PER_SEARCH = 5
from Connect import Connect
TWEETS_PER_SEARCH = 5 # Max Value = 100
class SearchTweetsByData: #class which represents data on a given tweet

    arg = "" #What search ? : ByHashTag, ByWord/Phrase, ByUser, Tweets since a date
    sender_name = ""
    date_tweet = ""
    newTweets = ""
    text = ""
    
    def __init__(self, arg, value):
        self.arg = arg
        # API Authentification
        api = self.initializeAPI()
        if self.arg == "Emetteur":
                self.sender_name = value
        elif self.arg == "Date":
            self.date_tweet = value

        elif self.arg == "Text":
            self.text = value

        elif self.arg == "Hashtag":
            self.text = "#"+value
        
    
    def getTweetsByData(self):
        api = self.initializeAPI()
        if self.arg == "Emetteur":
            self.newTweets = api.search(q="from:"+self.sender_name, lang="fr", count=TWEETS_PER_SEARCH)
            
        elif self.arg == "Date":
            self.newTweets = api.search(q="since:"+self.date_tweet, lang="fr", count=TWEETS_PER_SEARCH)

        elif self.arg == "Text" or self.arg =="Hashtag":
            self.newTweets = api.search(q=self.text, lang="fr", count=TWEETS_PER_SEARCH)

        return self.newTweets 

    def initializeAPI(self):
       co = Connect()
       return co.authentification()

    def displayTweetsByData(self):# for testing the class
        

        for tweet in self.newTweets:
            print(tweet.text)
            print("-----------------------------------------------------------")

    
s = SearchTweetsByData("Hashtag","France")
s.getTweetsByData()
print(s.displayTweetsByData())




