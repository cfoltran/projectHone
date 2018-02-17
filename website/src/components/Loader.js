
import React, { Component } from 'react';
import '../style/css/loader.css';


class Loader extends Component {
    render() {
        return (
            <div className="loader-progress" id="loader-progress">
                <div className="loader-progress-head">
                    <div className="first-indicator"></div>
                    <div className="second-indicator"></div>
                </div>
                <div className="loader-logo">
                    <img className="loader-logo-img" src="img/logo.svg" alt="Logo chargement"/>
                </div>
            </div>
        );
    }
}

export default Loader;
