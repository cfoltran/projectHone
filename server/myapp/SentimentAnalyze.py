from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

"""Classe pour analyzer le sentiment de un text caracterisee par :
    text
    sentiment
"""


class Sentiment():

    """Constructor"""
    def __init__(self, text):
        self.text = text

    """Method pour analyzer un text"""
    def analyze_text(self):
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        blob = tb(self.text)
        return blob.sentiment
