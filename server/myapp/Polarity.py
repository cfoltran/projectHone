from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

textblob = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())


class Polarity:
    def __init__(self, tweet):
        self.tweet = tweet

    def getPolarityTweet(self):
        polarity = textblob(self.tweet).sentiment
        return polarity[0]


pola = Polarity("j'aime j'aime")
print(pola.getPolarityTweet())
