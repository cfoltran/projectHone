//GOMEZ MATIAS - MHD TPH2
//require(codePython.py)

console.log("debut");

var request = require('superagent')


var Twit = require('twit') //necessité de l'API twitter

var T = new Twit({		//liaison au compte twitter du bot
	consumer_key:         'sIklgXwMbZZK5cL6hSRs6Vm4O',
	consumer_secret:      'xci297OYqxyjCR0hu2jiTJoel5AxUM2ktkYdO4e6sZHamr6JCM',
	access_token:         '959135997836644352-ZZNQJRW3HY6iWfJ7XWyYneOHS8cOuTg',
	access_token_secret:  'Bi7DBcOLWDYJS6E0OoVVygtDREcaRcj68i0bzvED1lMAT',
	//timeout_ms:          60*1000,  // optional HTTP request timeout to apply to all requests.

})

console.log("bonjour1")



function init(){
	console.log("bonjour2")
	//lance stream
	searchAllTweets();
}


function searchAllTweets (){
	// cette fonctionn appelle la fonction search pour tous les mots cle souhaites et renvoie le resultat comme une seuleliste de tweets
	return search_tweet("Jeux Olympiques") //faire attention à mettre les guillemets
}

/////////----RECHERCHE DE TWEET PAR MOTS-CLES----///////////

function search_tweet(search_content){
	// retourne une liste de tweets
	var params1 = {
 		q: search_content, //tweet contenant ce mots, hashtag compris
 		count: 1  	   //nombre de tweet recherché correspondant à 'q'
	}

	function gotData(err, data, response) {
		/* Cherchant exclusivement le texte des tweets recherchés
		nous n'affichons que le texte en créant une variable tweet contenant
		le status du data, puis on affiche que la partie '.text' */

  		console.log("bonjour3")

  		var tweetStatus = data.statuses;
  		var tweetText = "";
  		var name = data.screen_name;

  		console.log("bonjour4")

  		for (var i = 0; i < tweetStatus.length; i++) {
  			tweetText += tweetStatus[i].text;
  		}

  		console.log("bonjour5")

  		var polarite = analyseTweets(tweetText);
		// http://localhost:5001/polarity

		console.log("bonjour6")

		reactTweet(name, polarite);

		console.log("bonjour8")

	}

	T.get('search/tweets', params1, gotData);
	/* search/tweets : nom de la fonction de recherche de tweet par mots clé
	params : objet tweet recherché
	gotData: fonction appelée affichant les data recupéré */
}

function analyseTweets(msgToAnalyze){
	console.log(msgToAnalyze);
	request
  	.post('http://restfull-app:5001/sentiment/analyze')
  	.send({ text: msgToAnalyze })
  	.set('Accept', 'application/json')
  	.end(function(err, sentiment){
    	console.log(err);
			console.log(sentiment);
  	});

	/*
	fetch('http://localhost:5001/polarity', {
			method: 'POST',
=======
	fetch('http://localhost:5001/polarity', {
			method: 'POST',
>>>>>>> c538d28c8cf6f1fb7b806ded4e8d8179c7bab3af
			tweet: msgToAnalyze
			}).then(res => {
                console.log(res);
                return sentiment.json()
            })
            .then(res => {
                this.setState({polarite: sentiment.res});

            })
            .catch(error => console.error('Error:', error))


		*/
}

function reactTweet(name, polarity){


		//NEGATIF
		if (polarity<-0.25 ) {
			var tweetNeg = '@' + name + ' Ne soyez pas si pessimiste voyons :-(';
			tweetIT(tweetNeg);
		}
		//NEUTRE
		if (polarity>=0.25 && polarity<= 0.25) {
			var tweetNeut = '@' + name + ' Ma foi, c\'est bien vrai.';
			tweetIT(tweetNeut);
		}
		//POSITIF
			if (polarity>0.25) {
			var tweetPos = '@' + name + ' Ouai c\'est géniiial :-) !!!';
			tweetIT(tweetPos);
		}

		console.log("bonjour7")


}

function tweetIT(tweet_contents){
	var params2 ={ //definition du contenue du tweet
		status: tweet_contents
	}

	T.post('statuses/update', params2, post);

	function post(err, data, response) {
		if(err){
 		 console.log('We have a problem') //Ca ne marche pas
		}
		else{
			console.log('It\'s working') //Ca marche
		}
	}
}

init();
