import React from 'react';
import Switch from './Switch.js';
import { Navbar, NavbarBrand, NavbarNav, NavbarToggler, Collapse, NavItem} from 'mdbreact';
import { BrowserRouter as Router } from 'react-router-dom';
import {Button, Modal, ModalHeader, ModalBody, ModalFooter} from 'reactstrap';
import {withRouter} from "react-router-dom";


import Scrollchor from 'react-scrollchor';

class NavbarFeatures extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            collapse: false,
            isWideEnough: false,
            dropdownOpen: false,
            modal: false
        };

        this.toggle = this.toggle.bind(this);
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
    searchTag = event => {
        this.toggle();
        event.preventDefault();

        const tagSementic = {
            tag: this.tag.value,
        };
        this.props.history.push(`/search/${tagSementic.tag}`);
    };

    toggle() {
        this.setState({
            modal: !this.state.modal
        });
    }



    render() {
        return (
            <div className="font-25">

            <Router>
                <Navbar color="unique-color-dark" dark expand="md" scrolling fixed="top" >
                    <NavbarBrand href="/">
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
                                        <i className="fas fa-comment"/> Présentation
                                    </Scrollchor>
                                </NavItem>

                            </NavbarNav>

                        <NavbarNav right>
                            <NavItem>
                                <Switch checked={this.props.checked} onSwitchHome={this.props.onSwitchHome}/>
                            </NavItem>
                            <NavItem>
                            <div>
                                {/*<!--===========================================-->*/}
                                {/*                 <!--Modal-->                     */}
                                {/*<!--===========================================-->*/}

                                <Button color="primary" onClick={this.toggle}> <i className="fas fa-search"><span> Rechercher</span></i></Button>
                                <Modal contentclassName="padding-150x" isOpen={this.state.modal}
                                       modalTransition={{timeout: 20}}
                                       backdropTransition={{timeout: 10}}
                                       toggle={this.toggle} className={this.props.className}>
                                    <ModalHeader toggle={this.toggle}>
                                        Recherche dun hashtag en fonction du sentimenent voulu!
                                    </ModalHeader>
                                    <ModalBody>
                                        <div className="container padding-10">
                                            <form onSubmit={e => this.searchTag(e)}>
                                                <input type="text" required="required" ref={input => {
                                                    this.tag = input
                                                }}/>

                                                <button className="btn btn-primary" ref="both_checked" type="onSubmit">
                                                    Rechercher
                                                </button>
                                            </form>
                                        </div>
                                    </ModalBody>
                                    <ModalFooter>
                                    </ModalFooter>
                                </Modal>
                            </div>
                            </NavItem>
                        </NavbarNav>
                    </Collapse>
                </Navbar>
            </Router>
            </div>
        );
    }
}
export default withRouter(NavbarFeatures);
