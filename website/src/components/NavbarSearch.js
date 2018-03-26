/*
<nav className="navbar navbar-expand-md navbar-light fixed-top " id="navbar">
<a className="navbar-brand abs" href="">JoAnalytweet</--a>
<button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#menu"
aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    </button>
<div className="navbar-collapse collapse" id="menu">
    <ul className="navbar-nav">
        <li className="nav-item page-scroll">
            <a className="nav-link"> <i className="fas fa-map"> Map</i></a>
        </li>
        <li className="nav-item page-scroll">
            <a className="nav-link" > <i
                className="fas fa-home"> Accueil</i></a>
        </li>
        <li className="nav-item page-scroll">
            <a className="nav-link"><i className="fas fa-question-circle"> Présentation</i> </a>
        </li>
    </ul>
    */

//React
import React, {Component} from 'react';

import {Navbar, Nav, NavItem, NavDropdown, MenuItem} from 'react-bootstrap'

//Modal
import ModalSearch from './ModalSearch';

class NavbarSearch extends Component{

    render(){
        return(
            <Navbar inverse collapseOnSelect>
                <Navbar.Header>
                    <Navbar.Brand>
                        <a href="#brand">React-Bootstrap</a>
                    </Navbar.Brand>
                    <Navbar.Toggle />
                </Navbar.Header>
                    <Nav>
                        <NavItem eventKey={1} href="#">
                            Link
                        </NavItem>
                    </Nav>
                <Nav>
                        <NavItem eventKey={2} href="#">
                            Link
                        </NavItem>
                </Nav>
               
                    <Nav pullRight>

                        <NavItem eventKey={2} href="#">
                            <ModalSearch/>
                        </NavItem>
                    </Nav>
            </Navbar>
        );
    }
}
export default NavbarSearch;