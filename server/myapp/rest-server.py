#!flask/bin/python

import json
import os
from Tweet import Tweet
from SentimentAnalyze import Sentiment
from RetrieveRegionalTweets import RetrieveRegionalTweets
from StatisticsByRegion import StatisticsByRegion
from StatisticsByHashtag import StatisticsByHashtag
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


@app.route('/statistics/hashtag/<hashtagSearched>')
@cross_origin()
def getStatistics(hashtagSearched):
    statistics = StatisticsByHashtag(hashtagSearched)
    df = statistics.retrieveStatistics()
    result = df.to_dict(orient='index')
    # fix key error string
    result = {str(k):v for k,v in result.items()}
    json = jsonify({'statistics': result})
    return json


@app.route('/statistics/region/<codeRegion>')
@cross_origin()
def regionRouting(codeRegion):
<<<<<<< HEAD
    statistics = Statistics(None, codeRegion)
    df = statistics.retrieveTweets()
    result = df.to_dict(orient='index')
    # fix key error string
    result = {str(k):v for k,v in result.items()}
    json = jsonify({'statistics':result})
    return json
=======
>>>>>>> 7248061469bc8e8cb0b3159e219f4e8d927e03c2

    if(codeRegion == "all"):
        FILENAME = "regionalStats.json"
        if os.path.exists(FILENAME) and os.path.isfile(FILENAME) and os.path.getsize(FILENAME) > 0:
            with open(FILENAME, 'r') as f:
                data = json.load(f)
            return jsonify({'statistics': data})
    else:
        statistics = StatisticsByRegion(codeRegion)
        df = statistics.getStats()
        df.reset_index(inplace=True, drop=True)
        result = df.to_dict(orient='index')
        # fix key error string
        result = {str(k):v for k,v in result.items()}
        return jsonify({'statistics':result})

#localhost:5001/tweets/getTweetWithTime/JO2024
@app.route('/tweets/getTweetWithTime/<hashtagSearched>')
@cross_origin()
def get_tweet_with_time(hashtagSearched):

    myTweet = Tweet(hashtagSearched)
    tweets = myTweet.getTweetWithTime()
    result = tweets.to_dict(orient='index')
    result = {str(k):v for k,v in result.items()}
    listTweet = []
    for tweet in result.keys():
        listTweet.append(result[tweet])

    return jsonify({'tweets': listTweet})


@app.before_first_request
def active_job():
    # Start the thread
    retrieve = RetrieveRegionalTweets()
    retrieve.start()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
