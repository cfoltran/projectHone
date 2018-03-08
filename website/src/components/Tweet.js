import React, { Component } from 'react';

class Tweet extends Component {
  render() {
    return (
      <div className="tweet">
        <h1>{ this.props.author }</h1>
        <p>{ this.props.text }</p>
        <p>Analyse: { this.props.sentiment} </p>
      </div>
    );
  }
}

export default Tweet;
