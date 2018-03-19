import React from 'react';
import Tweet from './Tweet';

export default class Tweets extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            tweets: null
        };
    }

    componentDidMount() {
        this.loadData()
        this.forceUpdate()
        console.log(this.state)
    }

    loadData() {
        window.fetch('http://localhost:5001/tweets/getTweetWithTime/*')
            .then(
                response => {
                    response.json().then(result => {
                        //console.log()
                        this.setState({ tweets: result.tweets })
                    })
                })
            //.then(console.log(this.state.tweets))
            //.then(data => console.log(response)) /* this.setState({ tweets: data.tweets */
            .catch(error => console.error('Error:', error))
        console.log(this.state.tweets)
    }

    render() {
        return (
            <div>
                <section className="bg-light" id="home">
                    <div className="container padding-150" >
                        <div className="row text-center">
                            <div className="col-md-12" id="tweets">
                                <h1 className="font-70 text-dark">Tweets </h1><br/>
                                <main>
                                    {/*
                                        this.state.tweets.map(function(tweet){
                                            return <Tweet author={tweet.author} text={tweet.tweet}/>;
                                        })
                                    */}
                                </main>
                            </div>
                        </div>
                    </div>
                </section>

                <section className="bg-light" id="presentation">
                    <div className="container padding-150">
                        <div className="row text-center">
                            <div className="col-md-12">
                                <h1 className="font-70 text-dark">Presentation<br/></h1>
                                <hr/><br/>
                                    <p className="font-40 text-cloud text-dark">Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab aliquid consectetur cumque,
                                        deleniti doloremque ex expedita fugiat labore laborum mollitia officia, perferendis porro quod sapiente sed sequi soluta ut!</p>
                            </div>
                        </div>
                    </div>
                </section>

            </div>
        );
    }
}
