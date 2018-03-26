'use strict';

const express = require('express');

// Constants
const PORT = 8081;
const HOST = '0.0.0.0';
const bot = require('./bot');
const app = express();

function infiniteLoop() {
    setTimeout(() => {
      bot.searchAllTweets(); // to search all tweets

      infiniteLoop();//repeat it again
    }, 3000) //define the time you will repeat it 3000 = 3s
}

infiniteLoop();

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
