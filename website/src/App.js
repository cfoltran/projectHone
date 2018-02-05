import React, { Component } from 'react';
import Loader from './components/loader';
import Map from './components/map';
import './App.css';

class App extends Component {
    componentDidMount(){
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
        return (
            <div>
                <Loader/>
                <Map/>
            </div>
        );
    }
}

export default App;
