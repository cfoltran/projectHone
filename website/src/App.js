import React, { Component } from 'react';
import Loader from './components/loader';
import Map from './components/map';
import './style/css/App.css';
import Searchbar from "./components/searchbar";
import Search from "./components/Search";

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


