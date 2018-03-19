import tweepy

class Connect:
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    auth = ""
    api = ""

    def __init__(self):
        with open('Credentials.txt') as c:
            for line in c:
                if line.startswith("CONSUMER_KEY"):
                    l = line.split("=")
                    self.consumer_key = str(l[1]).strip()
                elif line.startswith("CONSUMER_SECRET"):
                    l = line.split("=")
                    self.consumer_secret = str(l[1]).strip()
                elif line.startswith("ACCESS_TOKEN"):
                    l = line.split("=")
                    self.access_token = str(l[1]).strip()
                elif line.startswith("ACCESS_SECRET"):
                    l = line.split("=")
                    self.access_token_secret = str(l[1]).strip()

    def authentication(self):
        print(self.consumer_key)
        print(self.consumer_secret)
        print(self.access_token_secret)
        print(self.access_token)
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
        return self.api

co = Connect()
co.authentication()