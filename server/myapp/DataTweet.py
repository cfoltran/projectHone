class DataTweet: #class which represents data on a given tweet
        text
    location_tweet
    sender_name
    nbRetweet
    nbLike
    nbAnswer

    def __init__(self, tweet):
        self.date_tweet = tweet.created_at
        self.location_tweet = tweet.place.name
        self.sender_name = tweet.user.name
        self.nbRetweet = tweet.retweet_count
        self.nbLike = tweet.favorite_count
        self.text = tweet.text
        self.nbAnswer = tweet.reply_count

