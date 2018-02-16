/*
///////////////////////////////////////////////////////////////
                File only for the route
///////////////////////////////////////////////////////////////
 */

//React
import React from 'react';
import {render} from 'react-dom';

//componant
import App from './App';
import Search from './components/Search';
import Searchbar from './components/Searchbar';
import Tweets from './components/Tweets';
import ChatBot from './components/Chatbot';
//config
import registerServiceWorker from './registerServiceWorker';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';


const Root = () =>{
    return(
        //route
        <Router>
            <Switch>
                <Route path="/" component={App}/>
                <Route exact path="/search/:tag" component={Search}/>
            </Switch>
        </Router>
    )

};

render(<Root />, document.getElementById('root'));
render(<Searchbar />, document.getElementById('searchbar'));
render(<Tweets />, document.getElementById('tweets'));
render(<ChatBot />, document.getElementById('chatbot'));
registerServiceWorker();
