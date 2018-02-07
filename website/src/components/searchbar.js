/*
///////////////////////////////////////////////////////////////
                Modal for search bar
///////////////////////////////////////////////////////////////
 */
import React, { Component } from 'react';
import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import { browserHistory } from 'history';
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

    searchTag = event =>{
        //Function will search hashtag

        const tag ={
            tag: this.tag.value,
            sementic: this.sementic.value
        };
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
                            <form onSubmit={this.toggle}>
                                <input type="text" required="required" ref={input =>{this.tag = input}}/>
                                    <label className="radio-inline padding-10">
                                        <input type="radio" name="optradio"/>Positif
                                    </label>
                                    <label className="radio-inline padding-10">
                                        <input type="radio" name="optradio"/>Négatif
                                    </label>
                                    <label className="radio-inline padding-10">
                                        <input type="radio" name="optradio" defaultChecked="defaultChecked"/>Les deux
                                    </label>
                                <button className="btn btn-primary" type="onSubmit" to={{pathname:`/search/` }}>Rechercher</button>
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