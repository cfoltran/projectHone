//React
import React, { Component } from 'react';

//Component
import Loader from './Loader';
import Map from './Map';
import NavbarFeatures from './NavbarFeatures';
import ChatBot from 'react-simple-chatbot';
import Tweets from "./Tweets";
import CarouselTweet from "./CarouselTweet";
import FooterPage from "./Footer";


//Config
import { ThemeProvider } from 'styled-components';
import steps from '../config/steps';
import bot from '../config/bot';

//Style
import '../style/css/App.css';

import '../style/css/bot.css';


class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            open: false,
            checked: false
        };

        this.toggleFloating = this.toggleFloating.bind(this);
        this.switchHome = this.switchHome.bind(this);
    }

    toggleFloating() {
        this.setState({
            open: !this.state.open
        });
    }

    componentDidMount() {
        const load = document.getElementById('loader-progress');
        if(load){
            setTimeout(() => {
                load.classList.add('available');
                setTimeout(() => {
                    load.outerHTML = '';
                }, 2000)
            }, 1000)
        }
    }

    switchHome = checked => {
        this.setState( { checked: checked} );
    };

    render() {
        // const tag = <Search ref={this.state.tag}/>;
        let classSwitch=(this.state.checked)?"padding-150 bg-dark":"padding-150 bg-light";
        let styleBg=(this.props.checked)?"bg-dark":"bg-light";
        let styleTitre=(this.props.checked)?"font-70 text-light":"font-70 text-dark";
        let styleText=(this.props.checked)?"font-40 text-light":"font-40 text-dark";
        return (
            <div>
            <section className={styleBg} id="toto">
               <CarouselTweet/>
                </section>
                <NavbarFeatures checked={this.state.checked} onSwitchHome={this.switchHome}/>
                <Loader/>
                <section className={classSwitch}>
                           <div className="container">
                               <div className="row">
                                   <div className="col-md-12">
                                       <Map/>
                                   </div>
                               </div>
                           </div>
                       </section>

                <ThemeProvider theme={bot}>
                <ChatBot
                steps={steps}
                floating={true}
                toggleFloating={this.toggleFloating}
                opened={this.state.open}
                headerTitle="Twot"
                botAvatar="./img/logo.png"
                placeholder="Tapez votre recherche..."
                />
                </ThemeProvider>
                 <section className={styleBg} id="presentation">
                    <div className="container padding-150">
                        <div className="row text-center">
                            <div className="col-md-12">
                                <h1 className={styleTitre}>Presentation<br/></h1>
                                <hr/><br/>
                                    <p className={styleText}>Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab aliquid consectetur cumque,
                                        deleniti doloremque ex expedita fugiat labore laborum mollitia officia, perferendis porro quod sapiente sed sequi soluta ut!</p>
                            </div>
                        </div>
                    </div>
                </section>
                <FooterPage/>
        </div>
        );
    }
}

export default Home;
