import React, { Component } from 'react';
import ModalSearch from './ModalSearch';
import Switch from './Switch.js';
import { Navbar, NavbarBrand, NavbarNav, NavbarToggler, Collapse, NavItem} from 'mdbreact';
import { BrowserRouter as Router } from 'react-router-dom';

import Scrollchor from 'react-scrollchor';

class NavbarFeatures extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            collapse: false,
            isWideEnough: false,
            dropdownOpen: false
        };
        this.onClick = this.onClick.bind(this);
        this.toggle = this.toggle.bind(this);
    }

    onClick(){
        this.setState({
            collapse: !this.state.collapse,
        });
    }

    toggle() {
        this.setState({
            dropdownOpen: !this.state.dropdownOpen
        });
    }

    render() {
        return (
            <div className="font-25">

            <Router>
                <Navbar color="unique-color-dark" dark expand="md" scrolling fixed="top" >
                    <NavbarBrand left href="/">
                        <img src="/img/logo.svg" alt="" height="100" width="100"/>
                        <strong className="font-30 padding-right-100">JoAnalytweet</strong>
                    </NavbarBrand>
                    { !this.state.isWideEnough && <NavbarToggler onClick = { this.onClick } />}
                    <Collapse isOpen = { this.state.collapse } navbar>
                            <NavbarNav left>
                                <NavItem>
                                    <Scrollchor  className="nav-link" to="#">
                                        <i className="fas fa-home"/> Accueil
                                    </Scrollchor>
                                </NavItem>
                                <NavItem >
                                    <Scrollchor  className="nav-link" to="#map">
                                        <i className="fas fa-map"/> Map
                                    </Scrollchor>
                                </NavItem>
                                <NavItem>
                                    <Scrollchor  className="nav-link"  to="#tweets">
                                        <i className="fas fa-twitter"/> Tweet
                                    </Scrollchor>
                                </NavItem>
                                <NavItem>
                                    <Scrollchor  className="nav-link"  to="#presentation">
                                        <i className="fas fa-hand-pointer-o"/> Présentation
                                    </Scrollchor>
                                </NavItem>

                            </NavbarNav>

                        <NavbarNav right>
                            <NavItem>
                                <Switch checked={this.props.checked} onSwitchHome={this.props.onSwitchHome}/>
                            </NavItem>
                            <NavItem>
                                <ModalSearch/>
                            </NavItem>
                        </NavbarNav>
                    </Collapse>
                </Navbar>
            </Router>
            </div>
        );
    }
}
export default NavbarFeatures;