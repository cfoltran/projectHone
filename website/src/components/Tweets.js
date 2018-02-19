import React from 'react';
import Tweet from './Tweet';

export default class Tweets extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            tweets: []
        }
        this.loadData();
    }

    loadData(path) {
        //
        window.fetch('http://127.0.0.1:5001/tweets/GottaGetEmAll')
        //  window.fetch('./data/exemple.json')
            .then(res => {
                console.log(res);
                return res.json()
            })
            .then(res => {
                this.setState({tweets: res.tweets});

            })
            .catch(error => console.error('Error:', error))
    }

    render() {
        return (
            <div>
                <h1 className="font-70 text-dark">Tweets </h1><br/>
                <main>
                    {
                        this.state.tweets.map((tweet, i) => {
                            return <Tweet author={tweet.author} text={tweet.text} key={'tweet' + i}/>
                        })
                    }
                </main>
            </div>
        );
    }
}