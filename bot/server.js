'use strict';

const express = require('express');

// Constants
const PORT = 8081;
const HOST = '0.0.0.0';

const app = express();

function infiniteLoop() {
    setTimeout(() => {
        var myTweet = tweetsToAnswer();// calling your code to get the tweets

        var polarity  = getPolarity(myTweet) //api restful for polarity

        answerTweet(myTweet, polarity);// using your code in nodejs to write the answer on twitter

        infiniteLoop();//repeat it again
    }, 3000) //define the time you will repeat it 3000 = 3s
}

infiniteLoop();


function tweetsToAnswer() {
    return Math.floor((Math.random() * 100) + 1);
}

  // you have to call the restful api to get the polarity
function getPolarity(myTweet){
  return (Math.random() * (1 - (-1)) + (-1)).toFixed(4);
}

// you will use the nodejs twitter api to answer
function answerTweet(myTweet,polarity){
  if (polarity>0.25)
    console.log('Responding to Twitte : ', myTweet, ' as positive , polarity: ', polarity);
    else if(polarity<0)
      console.log('Responding to Twitte : ', myTweet, ' as negative, polarity: ', polarity);
}

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
