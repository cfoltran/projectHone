//React
import React, { Component } from 'react';

//Component
import Loader from './Loader';
import Map from './Map';
import NavbarSearch from './NavbarSearch';
import ChatBot from 'react-simple-chatbot';
import Tweets from "./Tweets";

//Config
import { ThemeProvider } from 'styled-components';
import steps from '../config/steps';
import bot from '../config/bot';

//Style
import '../style/css/App.css';
import '../style/css/bot.css'





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
        return (
            <div>
                <NavbarSearch checked={this.state.checked} onSwitchHome={this.switchHome}/>
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
                <Tweets checked={this.state.checked} onSwitchHome={this.switchHome}/>
        </div>
        );
    }

}

export default Home;
