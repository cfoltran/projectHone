
import React, { Component } from 'react';
import '../style/css/loader.css';
import NavBarFeatures from './NavbarFeatures'


class Loader extends Component {
    render() {
        return (
            <div className="loader-progress" id="loader-progress">
                <NavBarFeatures/>
                <div className="loader-progress-head">
                    <div className="first-indicator"/>
                    <div className="second-indicator"/>
                </div>
                <div className="loader-logo">
                    <img className="loader-logo-img" src="img/logo.svg" alt="Logo chargement"/>
                </div>
            </div>
        );
    }
}

export default Loader;
