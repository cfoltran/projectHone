//GOMEZ MATIAS - MHD TPH2
//require(codePython.py)

var Twit = require('twit') //necessité de l'API twitter

var T = new Twit({		//liaison au compte twitter du bot
	consumer_key:         'sIklgXwMbZZK5cL6hSRs6Vm4O',
	consumer_secret:      'xci297OYqxyjCR0hu2jiTJoel5AxUM2ktkYdO4e6sZHamr6JCM',
	access_token:         '959135997836644352-ZZNQJRW3HY6iWfJ7XWyYneOHS8cOuTg',
	access_token_secret:  'Bi7DBcOLWDYJS6E0OoVVygtDREcaRcj68i0bzvED1lMAT',
	//timeout_ms:          60*1000,  // optional HTTP request timeout to apply to all requests. 

})


init();

function init(){
	//lance stream
	bot();
}

function bot(){
	console.log("bonjour")
	var tweets = searchAllTweets()	
	console.log("au recevoir");
}

function searchAllTweets (){
	// cette fonctionn appelle la fonction search pour tous les mots cle souhaites et renvoie le resultat comme une seuleliste de tweets
	return search_tweet("2018") //faire attention à mettre les guillemets
}

/////////----RECHERCHE DE TWEET PAR MOTS-CLES----///////////

function search_tweet(search_content){
	// retourne une liste de tweets
	var params1 = {
 		q: search_content, //tweet contenant ce mots, hashtag compris
 		count: 2  	   //nombre de tweet recherché correspondant à 'q'
	}

	function gotData(err, data, response) {
		/* Cherchant exclusivement le texte des tweets recherchés
		nous n'affichons que le texte en créant une variable tweet contenant
		le status du data, puis on affiche que la partie '.text' */
  		return data
		// http://localhost:5001/polarity
		}
		/*
		window.fetch("http://localhost:5001/polarity", {
  		method: "POST",
  		tweets: twi
		}).then(function (polarites){
				console.log(polarites);

			}) */

	}

	T.get('search/tweets', params1, gotData); 
	/* search/tweets : nom de la fonction de recherche de tweet par mots clé
	params : objet tweet recherché
	gotData: fonction appelée affichant les data recupéré */
}


///////////////////////////////////////////////////////////

/*
/////////----POSTER UN TWEET----///////////

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

//EXEMPLE : tweetIT('Joyeux JO !')   //utilsation de la fonction

//////////////////////////////////////////


/////////----REPONSE EN CAS DE FOLLOW----///////////

//fonction d'envoie de message lors de l'arriver d'un nouveau follower
function followed(eventMsg){
	var name = eventMsg.source.name; //on extrait le nom du nouveau follower
	var screenName = eventMsg.source.screen_name;
	tweetIT("@" + screenName + " thanks for the follow ;)") //Et on le/la remercie
	console.log("Followed event !") //Annonce console que le compte vient de se faire follow
}
/*
var stream = T.stream('user');  //creation d'un stream qui gardera activer la fonction followed
stream.on('follow', followed);  //Car on peut se faire follow à n'importe quel moment
*/

////////////////////////////////////////////////////


/////////----REPONSE A UN TWEET----///////////
/*
//fonction de reaction à un tweet
function tweetEvent(eventMsg){
	var replyto = eventMsg.in_reply_to_screen_name;
	var text = eventMsg.text;
	var from = eventMsg.user.screen_name;  //extraction du username 

	console.log(replyto + ' ' + from)  

	if(replyto === 'Twot_Bot'){
		var newTweet = '@' + from + ' thanks for tweet me :-)';
		tweetIT(newTweet);
	}
}
*/
/*
var stream = T.stream('user');  //creation d'un stream qui gardera activer la fonction followed
stream.on('tweet', tweetEvent);  //Car on peut recevoir un tweet à n'importe quel moment
*/

////////////////////////////////////////////////////

/////////----REPONSE SI POSITIVE/NEGATIVE----/////////

//var stream = T.stream(reactTweet)


/*
function reactTweet(tweet){
	windows.fetch('http://127.0.0.1:5001/tweets/polarityName').then(res=>{
		
		var tauxPN= res.json()

		//NEGATIF
		if (tauxPN.polarity<-0.25 ) {

			from =
			var tweetNeg = '@' + tauxPN.name + ' Ne soyez pas si pessimiste voyons :-(';
			tweetIT(tweetNeg);
		}
		//NEUTRE
		if (tauxPN.polarity>=0.25 && .polarity<= 0.25) {
			from =
			var tweetNeut = '@' + tauxPN.name + ' Ma foi, c\'est bien vrai.';
			tweetIT(tweetNeut);
		}
		//POSITIF
			if (tauxPN.polarity>0.25) {
			from =
			var tweetPos = '@' + tauxPN.name + ' Ouai c\'est géniiial :-) !!!';
			tweetIT(tweetPos);
		}

	})
}
*/

////////////////////////////////////////////////////


/////////----QUESTIONS/REPONSES----/////////
