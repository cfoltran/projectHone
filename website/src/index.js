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

//config
import registerServiceWorker from './registerServiceWorker';


const Root = () =>{
    return(
        <App/>
    )
};

render(<Root />, document.getElementById('root'));
registerServiceWorker();
