import json
class DataTweet: #class which represents data on a given tweet
        tweet
        text
    location_tweet
    sender_name
    nbRetweet
    nbLike
    nbAnswer

    def __init__(self, tweet):
        self.tweet = tweet
        self.date_tweet = tweet.created_at
        self.location_tweet = tweet.place.name
        self.sender_name = tweet.user.name
        self.nbRetweet = tweet.retweet_count
        self.nbLike = tweet.favorite_count
        self.text = tweet.text
        self.nbAnswer = tweet.reply_count

    def getText(self):
        return json.dumps(self.tweet.text)

    def getLocation(self):
        return json.dumps(self.tweet.location_tweet)

    def getSender(self):
        return json.dumps(self.tweet.sender_name)

    def getNbRetweet(self):
        return json.dumps(self.tweet.nbRetweet)

    def getNbLike(self):
        return json.dumps(self.tweet.nbLike)

    def getNbAnswer(self):
        return json.dumps(self.tweet.nbAnswer)

