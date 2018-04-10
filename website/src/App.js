//React
import React, { Component } from 'react';

//config
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

//Components
import Home from './components/Home'
import Search from './components/Search';
import MapFocus from './components/MapFocus';
import GenericNotFound from './components/GenericNotFound'



class App extends Component {

    render() {
        // const tag = <Search ref={this.state.tag}/>;
        return (
            <Router>
                <Switch>
                    <Route exact path="/" component={Home}/>
                    <Route  path="/search/:tag" component={Search}/>
                    <Route  path="/map/:region" component={MapFocus}/>
                    <Route component={GenericNotFound} />
                </Switch>
            </Router>
        );
    }

}

export default App;
