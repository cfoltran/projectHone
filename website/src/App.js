import React, { Component } from 'react';
import Loader from './components/Loader';
import Map from './components/Map';
import './style/css/App.css';

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
    // const tag = <Search ref={this.state.tag}/>;
        return (
            <div>
                <Loader/>
                <Map/>
            </div>
        );
    }
}

export default App;


