import React, { Component } from 'react';

export default class SearchTweets extends Component {
    constructor(props) {
        super(props);
        this.state = {
            tag: this.props.tag,
            sementic: this.props.sementic
        }
    }

    render() {
        return (
            <div className="searchtweets-container">
                <div className="searchtweets-container__title">
                    <h1>Tweets {this.state.sementic} avec l'#{this.state.tag}</h1>
                </div>
            </div>
        );
    }
}