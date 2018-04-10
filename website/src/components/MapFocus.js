import React, { Component } from 'react';
import NavbarFeatures from "./NavbarFeatures";
import * as d3 from 'd3';


//Style
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../style/css/style.css';
import FooterPage from "./Footer";


class MapFocus extends Component {

    componentDidMount() {
        this.initMap()
    }
    
    initMap() {
        //SVG region file
        var region = "/img/r/"+ this.props.match.params.region +".svg"
        var color = this.props.match.params.color;

        // set up svg image tag
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
            imgTest.src = region
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
                                    <svg id="map" ref="mapRender"></svg>
                                </div>
                            </div>
                            <div className="col-md-12">
                                <h2 className="font-60 bg-white">{ this.props.match.params.region }</h2>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
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