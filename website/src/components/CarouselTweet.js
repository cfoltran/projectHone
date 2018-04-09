import React, { Component } from 'react';
import {
    Carousel,
    CarouselItem,
    CarouselControl,
    CarouselIndicators,
    CarouselCaption
} from 'reactstrap';

import '../style/css/style.css'


class CarouselTweet extends Component {
    constructor(props) {
        super(props);
        this.next = this.next.bind(this);
        this.previous = this.previous.bind(this);
        this.goToIndex = this.goToIndex.bind(this);
        this.onExiting = this.onExiting.bind(this);
        this.onExited = this.onExited.bind(this);
        this.state = {
            activeIndex: 0,
            tweets : [
                {

                    Content: '#JO Trente-deux Russes non-invités font appel pour participer aux Jeux d’hiver à #Pyeongchang2018 http://lemde.fr/2C03lpF',
                    Author: '@lemondefr',
                    Date:'20/02/2018',
                    Retweets: '25'
                },
                {
                    caption: 'Beyonce'
                },
                {

                    caption: 'Oprah'
                },
                {

                    caption: 'Myrell Streep'
                }
            ]

        }
        window.fetch('http://localhost:5001/tweets/getTweetWithTime/Pyeongchang2018')
            .then(res => {
                return res.json()
            })
        .then(res => {
                this.setState( { tweets: res.tweets });
            })
        .catch(error => console.error('Error:', error))

    }

    onExiting() {
        this.animating = true;
    }

    onExited() {
        this.animating = false;
    }

    next() {
        if (this.animating) return;
        const items= this.state.tweets
        const nextIndex = this.state.activeIndex === items.length - 1 ? 0 : this.state.activeIndex + 1;
        this.setState({ activeIndex: nextIndex });
    }

    previous() {
        const items= this.state.tweets
        if (this.animating) return;
        const nextIndex = this.state.activeIndex === 0 ? items.length - 1 : this.state.activeIndex - 1;
        this.setState({ activeIndex: nextIndex });
    }

    goToIndex(newIndex) {
        if (this.animating) return;
        this.setState({ activeIndex: newIndex });
    }

    render() {
        const { activeIndex, tweets } = this.state;

        const slides = tweets.map((item,index) => {
            return (
                            <CarouselItem
                                className="padding-150 h-500 "
                                onExiting={this.onExiting}
                                onExited={this.onExited}
                                key={'itemcarousel'+index}
                            >
                                <img src={item.src} alt="" />
                                <CarouselCaption   key={'captioncarousel'+index} className="text-cloud " captionText={ item.Date + " - " + item.Author + " - " + item.Retweets + " retweets "} captionHeader={item.Content} ></CarouselCaption>
                            </CarouselItem>

            );
        });

        return (
            <div>
                <Carousel
                    activeIndex={activeIndex}
                    next={this.next}
                    previous={this.previous}
                >
                    <CarouselIndicators items={tweets} activeIndex={activeIndex} onClickHandler={this.goToIndex} key="test" />
                    {slides}
                    <CarouselControl  className="text-dark " direction="prev" directionText="Previous" onClickHandler={this.previous} key="carouselprev" />
                    <CarouselControl className="text-dark "  direction="next" directionText="Next" onClickHandler={this.next} key="carouselnext" />
                </Carousel>
            </div>
        );
    }
}


export default CarouselTweet;
