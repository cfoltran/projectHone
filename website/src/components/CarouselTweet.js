import React, { Component } from 'react';
import {
    Carousel,
    CarouselItem,
    CarouselControl,
    CarouselIndicators,
    CarouselCaption
} from 'reactstrap';

import '../style/css/style.css'


class Example extends Component {
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

                    text: '#JO Trente-deux Russes non-invités font appel pour participer aux Jeux d’hiver à #Pyeongchang2018 http://lemde.fr/2C03lpF',
                    caption: '@lemondefr',
                    date:'20/02/2018',
                    nbretweets: '25'
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
        /*window.fetch('./data/exemple.json')
            .then(res => {
                console.log(res);
                return res.json()
            })
            .then(res => {
                this.setState( { tweets: res.tweets });

            })
            .catch(error => console.error('Error:', error))
*/
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
        const items= this.state.tweets
        const { activeIndex } = this.state;

        const slides = items.map((item) => {
            const caption =  item.date + " - " + item.caption + " - " + item.nbretweets + " retweets - "
            return (
                            <CarouselItem
                                className="bg-light padding-150 h-500 "
                                onExiting={this.onExiting}
                                onExited={this.onExited}
                                key={item.src}
                            >
                                <img date={item.date} src={item.src} alt={item.altText} />
                                <CarouselCaption  className="text-cloud " captionText={caption} captionHeader={item.text} ></CarouselCaption>
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
                    <CarouselIndicators items={items} activeIndex={activeIndex} onClickHandler={this.goToIndex} />
                    {slides}
                    <CarouselControl  className="text-dark " direction="prev" directionText="Previous" onClickHandler={this.previous} />
                    <CarouselControl className="text-dark "  direction="next" directionText="Next" onClickHandler={this.next}  />
                </Carousel>
            </div>
        );
    }
}


export default Example;