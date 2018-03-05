#!flask/bin/python
import six
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


tweets = [
    {
        "author": "@lemondefr",
            "text": "#JO Trente-deux Russes non-invités font appel pour participer aux Jeux d’hiver à #Pyeongchang2018 http://lemde.fr/2C03lpF"
    }
]

@app.route('/')
@cross_origin()
def send_warnning():
    return "You must to specify a full address"

@app.route('/tweets/GottaGetEmAll', methods=['GET'])
@cross_origin()
def get_tasks():
    return jsonify({'tweets': tweets})

def ditBonjour():
    print("Bonjour");
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
