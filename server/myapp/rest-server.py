#!flask/bin/python
import six

from Tweet import Tweet
from SentimentAnalyze import Sentiment
from Statistics import Statistics

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.errorhandler(400)
@cross_origin()
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
@cross_origin()
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
@cross_origin()
def send_warnning():
    return "You must to specify a full address"

@app.route('/sentiment/analyze', methods=['GET'])
@cross_origin()
def analyze_text():
    analyze = Sentiment(request.args.get("text"))
    return jsonify({'sentiment': analyze.analyze_text()})

@app.route('/tweets/getTweet', methods=['GET'])
@cross_origin()
def get_tweet():

    # je crée seulement un tweet comme exemple
    myTweet = Tweet()

    # j'ai analysé son sentiment
    myTweet.sentiment_analyze_tweet()

    # Je l'ai inclus dans une liste
    tweets = []
    tweets.append(myTweet.serialize())

    #je donne la réponse au serveur
    return jsonify({'tweets': tweets})

<<<<<<< HEAD
@app.route('/statistics/', methods=['GET'])
@cross_origin()
def getStatistics():
    statistics = Statistics(request.args.get("#"))
    return jsonify({'statistics': statistics.retrieveStatistics()})


#URL/region
@app.route('/region/', methods=['GET'])
@cross_origin()
def getTweetByRegion():
    tweets = TweetByRegion(request.args.get("region","#"))
    return jsonify({'tweetbyregion': tweets.retrieveTweets()})


=======
def ditBonjour():
    print("Bonjour");
>>>>>>> 945e1a962925efd14d816176fa2b8e6b02b7dc77
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
