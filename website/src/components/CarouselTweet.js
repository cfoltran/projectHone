import React, { Component } from 'react';
import {
    Carousel,
    CarouselItem,
    CarouselControl,
    CarouselIndicators,
    CarouselCaption
} from 'reactstrap';


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
                    caption: '@lemondefr'
                },
                {

                    caption: 'Slide 2'
                },
                {

                    caption: 'Slide 3'
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
            return (


                            <CarouselItem

                                className="bg-light padding-150"
                                onExiting={this.onExiting}
                                onExited={this.onExited}
                                key={item.src}
                            >
                                <img src={item.src} alt={item.altText} />
                                <CarouselCaption  captionText={item.caption} captionHeader={item.text} />
                            </CarouselItem>

            );
        });

        return (
            <div>
                <style>
                {
                    `.custom-tag {
                max-width: 100%;
                height: 500px;

              }
              .carousel-caption {
                color: red;
              }`
                }
                </style>
                <Carousel
                    activeIndex={activeIndex}
                    next={this.next}
                    previous={this.previous}
                >
                    <CarouselIndicators items={items} activeIndex={activeIndex} onClickHandler={this.goToIndex} />
                    {slides}
                    <CarouselControl direction="prev" directionText="Previous" onClickHandler={this.previous} />
                    <CarouselControl direction="next" directionText="Next" onClickHandler={this.next} />
                </Carousel>
            </div>
        );
    }
}


export default Example;