'use strict';

const express = require('express');

// Constants
const PORT = 8081;
const HOST = '0.0.0.0';

const app = express();

function logEvery2Seconds(i) {
    setTimeout(() => {
        console.log('Responding to Twitte id: ', i);
        logEvery2Seconds(++i);
          // you have to call the restful api to get the Tweets to respond
    }, 2000)
}

  // you have to call the restful api to get the Tweets to respond
logEvery2Seconds(1);

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
