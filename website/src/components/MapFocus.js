import React, { Component } from 'react';

//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';

class MapFocus extends Component {
    
    constructor (props) {
        super(props);
    }

    render() {
        return (
                <section className="bg-dark text-center">
                <p> { this.props.match.params.region}</p>
                    <div className="container">
                        <h2 className="font-60">Recherche:</h2>
                        <div className="row text-center">
                            <div className="col-md-12  padding-150">

                            </div>

                        </div>
                    </div>
                </section>   
        )
    }
}

export default MapFocus