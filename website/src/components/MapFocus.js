import React, { Component } from 'react';
import NavbarFeatures from "./NavbarFeatures";
import * as d3 from 'd3';


//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';
import FooterPage from "./Footer";
import '../style/css/loader.css';


class MapFocus extends Component {

    constructor(props) {
        super(props);
        this.state = {
            region : "/img/r/"+ this.props.match.params.region +".svg",
            color : this.props.match.params.color,
            polarity : this.props.match.params.polarity,
            percent : (this.props.match.params.polarity*100) / 2 +50
        }
    }

    componentDidMount() {
        this.initMap()
    }
    
    initMap() {
        var region = this.state.region
        var images = d3.select("svg")
        .append('svg:image')
        .attr("fill","red")
        .attr('width', 200)
        .attr('height', 200);

        // create a test image
        var imgTest = new Image();
        // if it loads successfully add it to the svg image
        imgTest.onload = function() {
            images.attr("xlink:href", imgTest.src)
        }
        // if it fails test another image
        imgTest.onerror = function() {
            imgTest.src = region;
        }
        // this will fail
        imgTest.src = "https://does.not/exist.png";
    }

//<img src={`/img/regions/${this.props.match.params.region}.png`} alt={this.props.match.params.region}/>
    render() {
        return (
            <div>
                <NavbarFeatures/>
                <section id="mapFocusComponent" className="text-center bg-white focusRegion">

                    <div className="container">
                        <div className="row text-center">
                            <div className="col-md-12">
                                <div className="opacity">
                                    <svg id="map" ref="mapRender" color={this.state.color}/>                              
                                </div>
                            </div>
                            <div className="col-md-12">
                                <h2 className="font-60 bg-white">{ this.props.match.params.region }</h2>
                                <div class="progress">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100" style={{width: this.state.percent+'%', backgroundColor: this.props.match.params.color}}>
                                        Polarité : { this.state.polarity }
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                <FooterPage/>
            </div>

        )
    }
}

export default MapFocus