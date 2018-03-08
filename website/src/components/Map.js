import React, { Component } from 'react';
import * as d3 from 'd3';
import '../style/css/map.css';

class Map extends Component {
    componentDidMount() {
        this.initMap()
    }

    componentDidUpdate(){
        this.initMap()
    }

    initMap() {
            // Width and height
            var width = 900
            var height = 900;

            //Define map projection
            var projection = d3.geoConicConformal()
                               .center([2.454071, 46.379229])
                               .scale(4000)
                               .translate([width / 2, height / 2]);

            //Define default path generator
            var path = d3.geoPath()
                         .projection(projection);
            
            //Define quantize scale to sort data values into buckets of color
            var color = d3.scaleQuantize()
                                .range(["#ff0000","#ff3300","#ff6600","#ff9933","#ffcc66"," #ffff99","#ccff99","#99ff66","#66ff33","#33cc33"]);

            //Create SVG element
            var svgMap = d3.select('#map').append("svg")
                .attr("id", "svg")
                .attr("width", width)
                .attr("height", height)
                .attr("fil","#212529");

            var deps = svgMap.append("g");

            var div = d3.select(this.refs.mapRender).append("div")
                .attr("class", "tooltip")
                .style("opacity", 0);

            // Load in france data
            d3.csv('/static/fr-data-test.csv', function(data) {
                // Set in put domain for color scale
                color.domain([
                    d3.min(data, function(d) { return d.value; }),
                    d3.max(data, function(d) { return d.value; }),
                ])

                //Load in GeoJSON data
                d3.json('/static/departments.json', function(geojson) { 
                    // Merge the fr. data and GeoJSON
                    // Loop through once for each fr. data value
                    for(var i = 0; i < data.length; i++) {
                        // Grab state name
                        var dataState = data[i].state;

                        // Grab data value, and convert form string to float
                        var dataValue = parseFloat(data[i].value);

                        // Find the corresponding state inside the GeoJSON
                        for(var j = 0; j < geojson.features.length; j++){
                            var jsonState = geojson.features[j].properties.nom;

                            if(dataState == jsonState){
                                // Copy the data value into the JSON
                                geojson.features[j].properties.value = dataValue;

                                // Stop looking through the JSON
                                break;
                            }
                        }
                    } 

                    //Bind data and create one path per GeoJSON feature
                    deps.selectAll("path")
                        .data(geojson.features)
                        .enter()
                        .append("path")
                        .attr("d", path)
                        .style("fill", function(d) {
                            /*
                            [-1, -0.3] : négatif
                            [-0.3, 0.3] : neutre
                            [0.3, 1] : positif
                            */
                            // Get data value
                            var value = d.properties.value;

                            if(value) {
                                // If value exists...
                                return color(value);
                            } else {
                                // If value is undefined
                                return "#ccc";
                            }
                        })
                        .on("mouseover", function(d) {
                            d3.select(this).attr("fill","black");
                            div.transition()
                                .duration(200)
                                .style("opacity", .9);
                            div.html("Région : " + d.properties.nom + "<br>"
                                +  "Code : " + d.properties.code)
                                .style("left", (d3.event.pageX + 30) + "px")
                                .style("top", (d3.event.pageY - 30) + "px")
                        })
                        .on("mouseout", function(d) {
                            d3.select(this).attr("fill","rgba(98,225,230,0.5)");
                            div.transition()
                                .duration(0)
                                .style("opacity", 0);
                            div.html("")
                                .style("left", "0px")
                                .style("top", "0px");
                        });
                })

            });
}

    render() {
        return (

            <div className="bg-dark" id="map" ref="mapRender"></div>
        )
    }
}

export default Map;
