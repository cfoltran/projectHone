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

//config
import registerServiceWorker from './registerServiceWorker';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';


const Root = () =>{
    return(
        <App/>
    )
};

render(<Root />, document.getElementById('root'));
registerServiceWorker();
