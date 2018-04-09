/*
///////////////////////////////////////////////////////////////
                Modal
///////////////////////////////////////////////////////////////
 */
//React
import React, {Component} from 'react';
//config
import {Button, Modal, ModalHeader, ModalBody, ModalFooter} from 'reactstrap';
import {withRouter} from "react-router-dom";
//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';


class ModalSearch extends Component {

    searchTag = event => {
        this.toggle();
        event.preventDefault();

        console.log(this.getValueChecked());

        const tagSementic = {
            tag: this.tag.value,
            sementic: this.getValueChecked()
        };
        this.props.history.push(`/search/${tagSementic.tag}/${tagSementic.sementic}`);
    };

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

    getValueChecked() {

        let sementic = "";
        if (this.good_checked.checked) {
            sementic = "positif";
        }
        else if (this.bad_checked.checked) {
            sementic = "negative";
        }
        else {
            sementic = "positif et negatif"
        }
        console.log(this.bad_checked.checked);
        return sementic;
    }

    render() {
        // let styleNav = (this.props.checked) ? "navbar navbar-expand-md navbar-dark bg-dark fixed-top " : "navbar navbar-expand-md bg-light navbar-light fixed-top ";
        return (
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
                        Recherche d'un hashtag en fonction du sentimenent voulu!
                    </ModalHeader>
                    <ModalBody>
                        <div className="container padding-10">
                            <form onSubmit={e => this.searchTag(e)}>
                                <input type="text" required="required" ref={input => {
                                    this.tag = input
                                }}/>
                                <label className="radio-inline padding-10">
                                    <input type="radio" ref={(input) => {
                                        this.good_checked = input
                                    }} name="optradio"/>Positif
                                </label>
                                <label className="radio-inline padding-10">
                                    <input type="radio" ref={(input) => {
                                        this.bad_checked = input
                                    }} name="optradio"/>Négatif
                                </label>
                                <label className="radio-inline padding-10">
                                    <input type="radio" name="optradio" defaultChecked="defaultChecked"
                                           ref={(input) => {
                                               this.both_checked = input
                                           }}/>Les deux
                                </label>
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
        );
    }
}

export default withRouter(ModalSearch);