from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

textblob = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())


class Polarity:
    def __init__(self, tweets):
        self.tweets = tweets

    def getPolarityTweet(self):
        result = {}
        for tweet in self.tweets:
            polarity = textblob(tweet).sentiment
            result[tweet] = polarity[0]
        return result

tweets = ["je t'aime","affreux affreux","tu vas mourir demain"]
test = Polarity(tweets)
print(test.getPolarityTweet())
