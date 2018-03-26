import React, { Component } from 'react';
import Searchbar from './Searchbar';


//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';

class MapFocus extends Component {
    
    constructor (props) {
        super(props);
    }

    render() {
        
        return (
                <section className="text-center bg-white">
                    <Searchbar/>
                    <div className="container">
                        <h2 className="font-60 bg-white">{ this.props.match.params.region }</h2>
                        <div className="row text-center">
                            <div className="col-md-3" >
                                <img src={`/img/regions/${this.props.match.params.region}.png`}/>
                            </div>
                            <div className="col-md-3">
                                <p>Lorem</p>
                            </div>
                

                        </div>
                    </div>
                </section>   
        )
    }
}

export default MapFocus