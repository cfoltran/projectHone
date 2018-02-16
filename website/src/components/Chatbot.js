import React, { Component } from 'react';
import ChatBot from 'react-simple-chatbot';
import '../style/css/bot.css';

export default class Chatbot extends Component {

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

    render() {


        return (
            <div>
                <ChatBot
                    steps={[
                        {
                            id: '1',
                            message: 'Vous cherchez des informations ?',
                            trigger: '2',
                        },
                        {
                            id: '2',
                            options: [
                                { value: 1, label: 'Le concept ?', trigger: '4' },
                                { value: 2, label: 'Notre Twitter', trigger: '3' },
                            ],
                        },
                        {
                            id: '3',
                            message: '<a href="https://twitter.com/Twot_Bot"></a>',
                            trigger: '1'
                        },
                        {
                            id: '4',
                            message: 'Le concept est ...',
                            trigger: '1'
                        },
                    ]}
                    floating={true}
                    toggleFloating={this.toggleFloating}
                    opened={this.state.open}
                    headerTitle="Twot"
                    botAvatar="./img/logo.svg"
                    placeholder="Tapez votre recherche..."
                />
            </div>
        );
    }
}
