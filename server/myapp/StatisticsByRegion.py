import json
import pandas
import numpy as np
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from TweetByRegion import TweetByRegion
from SentimentAnalyze import Sentiment


class StatisticsByRegion:
	def __init__(self, region):
		self.region = region


	def getStats(self):
		if self.region == "all":

			data = pandas.DataFrame()
			
			sAlsace = TweetByRegion("Alsace")
			res = sAlsace.retrieveTweets()
			df = self.resultToFrame(res, "Alsace")
			data = data.append(df)

			sAquitaine = TweetByRegion("Aquitaine")
			res = sAquitaine.retrieveTweets()
			df = self.resultToFrame(res, "Aquitaine")
			data = data.append(df)

			sAuvergne = TweetByRegion("Auvergne")
			res = sAuvergne.retrieveTweets()
			df = self.resultToFrame(res, "Auvergne")
			data = data.append(df)

			sBasse_Normandie = TweetByRegion("Basse_Normandie")
			res = sBasse_Normandie.retrieveTweets()
			df = self.resultToFrame(res, "Basse_Normandie")
			data = data.append(df)

			sBourgogne = TweetByRegion("Bourgogne")
			res = sBourgogne.retrieveTweets()
			df = self.resultToFrame(res, "Bourgogne")
			data = data.append(df)

			sBretagne = TweetByRegion("Bretagne")
			res = sBretagne.retrieveTweets()
			df = self.resultToFrame(res, "Bretagne")
			data = data.append(df)

			sCentre = TweetByRegion("Centre")
			res = sCentre.retrieveTweets()
			df = self.resultToFrame(res, "Centre")
			data = data.append(df)

			sChampagneArdenne = TweetByRegion("Champagne-Ardenne")
			res = sChampagneArdenne.retrieveTweets()
			df = self.resultToFrame(res, "Champagne-Ardenne")
			data = data.append(df)

			sCorse = TweetByRegion("Corse")
			res = sCorse.retrieveTweets()
			df = self.resultToFrame(res, "Corse")
			data = data.append(df)

			sFrancheComte = TweetByRegion("Franche-Comte")
			res = sFrancheComte.retrieveTweets()
			df = self.resultToFrame(res, "Franche-Comte")
			data = data.append(df)

			sHaute_Normandie = TweetByRegion("Haute_Normandie")
			res = sHaute_Normandie.retrieveTweets()
			df = self.resultToFrame(res, "Haute_Normandie")
			data = data.append(df)

			sIledeFrance = TweetByRegion("Ile-de-France")
			res = sIledeFrance.retrieveTweets()
			df = self.resultToFrame(res, "Ile-de-France")
			data = data.append(df)

			sLanguedocRoussillon = TweetByRegion("Languedoc-Roussillon")
			res = sLanguedocRoussillon.retrieveTweets()
			df = self.resultToFrame(res, "Languedoc-Roussillon")
			data = data.append(df)

			sLimousin = TweetByRegion("Limousin")
			res = sLimousin.retrieveTweets()
			df = self.resultToFrame(res, "Limousin")
			data = data.append(df)

			sLorraine = TweetByRegion("Lorraine")
			res = sLorraine.retrieveTweets()
			df = self.resultToFrame(res, "Lorraine")
			data = data.append(df)

			sMidiPyrenees = TweetByRegion("Midi-Pyrenees")
			res = sMidiPyrenees.retrieveTweets()
			df = self.resultToFrame(res, "Midi-Pyrenees")
			data = data.append(df)

			sNordPasdeCalais = TweetByRegion("Nord-Pas-de-Calais")
			res = sNordPasdeCalais.retrieveTweets()
			df = self.resultToFrame(res, "Nord-Pas-de-Calais")
			data = data.append(df)

			sPays_de_la_Loire = TweetByRegion("Pays_de_la_Loire")
			res = sPays_de_la_Loire.retrieveTweets()
			df = self.resultToFrame(res, "Pays_de_la_Loire")
			data = data.append(df)

			sPicardie = TweetByRegion("Picardie")
			res = sPicardie.retrieveTweets()
			df = self.resultToFrame(res, "Picardie")
			data = data.append(df)

			sPoitouCharentes = TweetByRegion("Poitou-Charentes")
			res = sPoitouCharentes.retrieveTweets()
			df = self.resultToFrame(res, "Poitou-Charentes")
			data = data.append(df)

			sProvenceAlpesCoteAzur = TweetByRegion("Provence-Alpes-Cote-d_Azur")
			res = sProvenceAlpesCoteAzur.retrieveTweets()
			df = self.resultToFrame(res, "Provence-Alpes-Cote-d_Azur")
			data = data.append(df)

			sRhoneAlpes = TweetByRegion("Rhone-Alpes")
			res = sRhoneAlpes.retrieveTweets()
			df = self.resultToFrame(res, "Rhone-Alpes")
			data = data.append(df)

			sGuadeloupe = TweetByRegion("Guadeloupe")
			res = sGuadeloupe.retrieveTweets()
			df = self.resultToFrame(res, "Guadeloupe")
			data = data.append(df)

			sMartinique = TweetByRegion("Martinique")
			res = sMartinique.retrieveTweets()
			df = self.resultToFrame(res, "Martinique")
			data = data.append(df)

			sGuyane = TweetByRegion("Guyane")
			res = sGuyane.retrieveTweets()
			df = self.resultToFrame(res, "Guyane")
			data = data.append(df)

			sLa_Reunion = TweetByRegion("La_Reunion")
			res = sLa_Reunion.retrieveTweets()
			df = self.resultToFrame(res, "La_Reunion")
			data = data.append(df)

			sMayotte = TweetByRegion("Mayotte")
			res = sMayotte.retrieveTweets()
			df = self.resultToFrame(res, "Mayotte")
			data = data.append(df)

			return data

		else:
			d = TweetByRegion(self.region)
			res = d.retrieveTweets()
			return self.resultToFrame(res, self.region)

	def resultToFrame(self, result, region):
		totalPolarity = 0.0
		totalRT = 0
		nbTweets = 0

		for tweet in result:
			nbTweets += 1
			sentiment = Sentiment(tweet.text)
			pol = sentiment.analyze_text()
			totalPolarity += pol[0]

		arrayRT = np.array([tweet.retweet_count for tweet in result])

		for tweet in arrayRT:
			totalRT += tweet

		data = pandas.DataFrame()
		if nbTweets != 0:
			data['AverageRetweets'] = np.array([totalRT / nbTweets])
			data['AveragePolarity'] = np.array([totalPolarity / nbTweets])
		else:
			data['AverageRetweets'] = np.array([0])
			data['AveragePolarity'] = np.array([0])
		data['NumbersOfTweets'] = np.array([nbTweets])
		data['Region'] = np.array([region])
		return data