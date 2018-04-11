import React, { Component } from 'react';
import {
UncontrolledCarousel
} from 'reactstrap';

import '../style/css/style.css'


class CarouselO extends Component {
  constructor(props) {
    super(props);
    this.next = this.next.bind(this);
    this.prev = this.prev.bind(this);
    this.state = {
      activeItem: 1,
      maxLength: 100,
      tweets : [
          {
              Content: '',
              Author: '',
              Date:'',
              Retweets: ''
          },
      ]
    };

    window.fetch('http://localhost:5001/tweets/getTweetWithTime/Pyeongchang2018')
        .then(res => {
            return res.json()
        })
    .then(res => {

            this.setState( { tweets: res.tweets });
        })
    .catch(error => console.error('Error:', error))

  }
    render() {
        <UncontrolledCarousel items={this.state.tweets} />
      );
  }
}
}


export default CarouselO;
