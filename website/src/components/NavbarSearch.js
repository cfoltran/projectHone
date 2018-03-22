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

class Navbar extends Component{

    render(){
        return(
            <Navbar inverse collapseOnSelect>
                <Navbar.Header>
                    <Navbar.Brand>
                        <a href="#brand">React-Bootstrap</a>
                    </Navbar.Brand>
                    <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
                    <Nav>
                        <NavItem eventKey={1} href="#">
                            Link
                        </NavItem>
                        <NavItem eventKey={2} href="#">
                            Link
                        </NavItem>
                        <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
                            <MenuItem eventKey={3.1}>Action</MenuItem>
                            <MenuItem eventKey={3.2}>Another action</MenuItem>
                            <MenuItem eventKey={3.3}>Something else here</MenuItem>
                            <MenuItem divider />
                            <MenuItem eventKey={3.3}>Separated link</MenuItem>
                        </NavDropdown>
                    </Nav>
                    <Nav pullRight>
                        <NavItem eventKey={1} href="#">
                            Link Right
                        </NavItem>
                        <NavItem eventKey={2} href="#">
                            Link Right
                        </NavItem>
                        <NavItem eventKey={2} href="#">
                            <ModalSearch/>
                        </NavItem>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        );
    }
}
export default Navbar;