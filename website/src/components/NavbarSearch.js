/*
///////////////////////////////////////////////////////////////
                        search bar
///////////////////////////////////////////////////////////////
 */

//React
import React, {Component} from 'react'

//React-Bootstrap
import {Navbar, Nav, NavItem} from 'react-bootstrap';

//ModalSearch
import ModalSearch from './ModalSearch';
import Switch from './Switch.js';

//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';


class NavbarSearch extends Component {

    render() {
        return (
            <Navbar inverse collapseOnSelect>
                <Navbar.Header>
                    <Navbar.Brand>
                        <a href="#">JoAnalytweet</a>
                    </Navbar.Brand>
                    <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
                <Nav>
                    <NavItem eventKey={1} href="Map.js#map"> <i className="fas fa-map"/>
                        Map
                    </NavItem>
                </Nav>
                </Navbar.Collapse>
                <Nav>
                    <NavItem eventKey={2} href="Tweets.js#home"> <i className="fas fa-home"/>
                        Accueil
                    </NavItem>
                </Nav>
                <Nav>
                    <NavItem eventKey={3} href="Tweets.js#presentation"> <i className="fas fa-hand-pointer-o"/>
                        Présentation
                    </NavItem>
                </Nav>
                <Nav>
                    <NavItem eventKey={4} href="../../node_modules\keycode\test\mocha.js#stats"> <i className="fas fa-line-chart"/>
                        Statistique
                    </NavItem>
                </Nav>
                <Nav>
                    <NavItem eventKey={5} href="#"> <i className="fas fa-chart-line"/>
                        <Switch checked={this.props.checked} onSwitchHome={this.props.onSwitchHome}/>
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