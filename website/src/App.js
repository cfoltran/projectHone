import React, { Component } from 'react';
import Loader from './components/Loader';
import Map from './components/Map';
import ChatBot from 'react-simple-chatbot';
import { ThemeProvider } from 'styled-components';
import steps from './config/steps';
import bot from './config/bot';
import './style/css/App.css';
import './style/css/bot.css';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            open: false
        };

        this.toggleFloating = this.toggleFloating.bind(this);
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

    render() {
        // const tag = <Search ref={this.state.tag}/>;
        return (
            <div>
                <Loader/>
                <Map/>
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
            </div>
        );
    }
}

export default App;
