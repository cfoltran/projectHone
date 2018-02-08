/*
///////////////////////////////////////////////////////////////
                Modal for search bar
///////////////////////////////////////////////////////////////
 */
import React, { Component } from 'react';
import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import {Link} from 'react-router-dom';
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';

class Searchbar extends Component {

    constructor(props) {
        super(props);
        this.state = {
            modal: false
        };

        this.toggle = this.toggle.bind(this);
    }

    toggle() {
            this.setState({
                modal: !this.state.modal
            });
    }

    //Function will search hashtag
    searchTag = event =>{
        event.preventDefault();

        const tag = this.tagInput.value;
        //sementic: this.sementic.text

        this.props.history.push(`/search/${tag}`);
    };

    render() {
        return (
            <div>
                <Button color="danger" onClick={this.toggle}>Rechercher <i className="fas fa-search"></i></Button>
                <Modal contentClassName="padding-150x" isOpen={this.state.modal} modalTransition={{ timeout: 20 }} backdropTransition={{ timeout: 10 }}
                       toggle={this.toggle} className={this.props.className}>
                    <ModalHeader toggle={this.toggle}>Recherche d'un hashtag en fonction du sentiment voulu!</ModalHeader>
                    <ModalBody>
                        <div className="container padding-10">
                            <form onSubmit={e => this.searchTag(e) && this.toggle() }>
                                <input type="text" required="required" ref={input =>{this.tagInput = input}}/>
                                    <label className="radio-inline padding-10">
                                        <input type="radio" name="optradio"/>Positif
                                    </label>
                                    <label className="radio-inline padding-10">
                                        <input type="radio" name="optradio"/>Négatif
                                    </label>
                                    <label className="radio-inline padding-10">
                                        <input type="radio" name="optradio" defaultChecked="defaultChecked"/>Les deux
                                    </label>
<<<<<<< HEAD
                                <button className="btn btn-primary" type="onSubmit">Search</button>
=======
                                <button className="btn btn-primary" type="onSubmit" to={{pathname:`/search/` }}>Rechercher</button>
>>>>>>> 8ce182121c1d5d4d3fdd0b50b3d0857bd1bd1ed7
                            </form>
                        </div>
                    </ModalBody>
                    <ModalFooter>
                    </ModalFooter>
                </Modal>
            </div>
        );
    }

}
export default Searchbar;