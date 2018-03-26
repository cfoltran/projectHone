/*
///////////////////////////////////////////////////////////////
                        search bar
///////////////////////////////////////////////////////////////
 */

//React
import React, {Component} from 'react';
//React-Bootstrap
import {Navbar, Nav, NavItem, NavDropdown, MenuItem} from 'react-bootstrap';
//ModalSearch
import ModalSearch from './ModalSearch';
//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';


class NavbarSearch extends Component {

    render() {
        return (
            <Navbar inverse collapseOnSelect expanded>
                <Navbar.Header>
                    <Navbar.Brand>
                        <a href="#">JoAnalytweet</a>
                    </Navbar.Brand>
                </Navbar.Header>
                <Nav>
                    <NavItem eventKey={1} href="#">
                        Map
                    </NavItem>
                </Nav>
                <Nav>
                    <NavItem eventKey={2} href="#">
                        Accueil
                    </NavItem>
                </Nav>
                <Nav>
                    <NavItem eventKey={3} href="#">
                        Présentation
                    </NavItem>
                </Nav>
                <Nav>
                    <NavItem eventKey={4} href="#">
                        Statistique
                    </NavItem>
                </Nav>
                <Nav pullRight>
                    <NavItem eventKey={1} href="#">
                        <ModalSearch/>
                    </NavItem>
                </Nav>
            </Navbar>
        );
    }
}

export default NavbarSearch;