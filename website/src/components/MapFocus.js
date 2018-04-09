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
                <section id="mapFocusComponent" className="text-center bg-white" class="focusRegion">
                    <Searchbar/>
                    <div className="container">
                        <div className="row text-center">
                            <div className="col-md-12">
                                <div class="opacity">
                                    <img src={`/img/regions/${this.props.match.params.region}.png`}/>
                                </div>
                            </div>
                            <div className="col-md-12">
                                <h2 className="font-60 bg-white">{ this.props.match.params.region }</h2>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
                            </div>
                        </div>
                    </div>
                </section>   
        )
    }
}

export default MapFocus