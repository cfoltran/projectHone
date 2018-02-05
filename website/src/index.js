import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import Searchbar from './components/searchbar';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
ReactDOM.render(<Searchbar />, document.getElementById('searchbar'));
registerServiceWorker();
