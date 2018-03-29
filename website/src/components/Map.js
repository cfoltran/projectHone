import React, { Component } from 'react';
import * as d3 from 'd3';
import '../style/css/map.css';

class Map extends Component {
    componentDidMount() {
        this.initMap()
    }

    // Source: http://shop.oreilly.com/product/0636920026938.do


    initMap() {
            // Width and height
            var width = 1000, height = 900;

            // Define map projection
            var projection = d3.geoConicConformal()
                               .center([2.454071, 46.379229])
                               .scale(4000)
                               .translate([width / 2, height / 2]);

            // Define default path generator
            var path = d3.geoPath()
                         .projection(projection);

            // Define quantize scale to sort data values into buckets of color
            var color = ["#FF453E","#E87B31","#FFEEC8","#E8E23D","#6CFF3A"];

            // Create SVG element
            var svgMap = d3.select(this.refs.mapRender).append("svg")
                                          .attr("id", "svg")
                                          .attr("width", width)
                                          .attr("height", height)
                                          .attr("fill","#212529");

            var deps = svgMap.append("g");

            var div = d3.select(this.refs.mapRender).append("div")
                                                    .attr("class", "tooltip")
                                                    .style("opacity", 0);

            // Load in france data
            d3.json('http://localhost:5001/statistics/region/all', function(data) {
                // Load in GeoJSON data

                // relation between map's json and tweets json
                var frStatesMap={'Ile-de-France': '0'
                'Auvergne-Rhone-Alpes': '1'
                'Occitanie': '10'
                'Pays_de_la_Loire': '11'
                'Provence-Alpes-Cote_dAzur': '12'
                'La_Reunion': '13'
                'Martinique': '14'
                'Guyane': '15'
                'Guadeloupe': '16'
                'Mayotte': '17',
                'Bourgogne-Franche-Comte': '2',
                'Bretagne': '3',
                'Centre-Val_de_Loire': '4',
                'Corse': '5',
                'Grand_Est': '6',
                'Hauts-de-France': '7',
                'Normandie': '8',
                'Nouvelle-Aquitaine': '9'}

                d3.json('/static/departments.json', function(geojson) {
                  console.log(geojson)
                    // Merge the fr. data and GeoJSON
                    // Loop through once for each fr. data value

                    //// removes the unformal chars

                    function pure(str){
                        var accents    = 'ÀÁÂÃÄÅàáâãäåÒÓÔÕÕÖØòóôõöøÈÉÊËèéêëðÇçÐÌÍÎÏìíîïÙÚÛÜùúûüÑñŠšŸÿýŽž';
                        var accentsOut = "AAAAAAaaaaaaOOOOOOOooooooEEEEeeeeeCcDIIIIiiiiUUUUuuuuNnSsYyyZz";
                        str = str.split('');
                        var strLen = str.length;
                        var i, x;
                        for (i = 0; i < strLen; i++) {
                          if ((x = accents.indexOf(str[i])) != -1) {
                            str[i] = accentsOut[x];
                          }
                        }
                        return str.join('');
                    }

                    // makes map.json and data from python relatable
                    for(var i = 0; i < geojson.features.length; i++) {
                      geojson.features[i].properties.value = data.statistics[frStatesMap[pure(geojson.features[j].properties.nom.replace(/\s/g,'_').replace(/'/g,''))]]
                          ['AveragePolarity'] || 0
                    }

                    function feeling(num)
                    {
                      if(num >= -1 && num < -0.65)
                          return "Énervé";
                      else if(num >= -0.65 && num < -0.3)
                          return "Pas content";
                      else if(num >= -0.3 && num < 0.3)
                          return "Neutre";
                      else if(num >= 0.3 && num < 0.65)
                          return "Content";
                      else if(num >= 0.65 && num <= 1)
                          return "Trés content";
                    }
                    // Bind data and create one path per GeoJSON feature
                    deps.selectAll("path")
                        .data(geojson.features)
                        .enter()
                        .append("path")
                        .attr("d", path)
                        .attr("stroke","black")
                        .style("fill", function(d) {
                            // Get data value
                            var value = d.properties.value;
                            var humeur
                            if(typeof(value) == "number") {
                                if(value >= -1 && value < -0.65)
                                    return color[0];
                                else if(value >= -0.65 && value < -0.3)
                                    return color[1];
                                else if(value >= -0.3 && value < 0.3)
                                    return color[2];
                                else if(value >= 0.3 && value < 0.65)
                                    return color[3];
                                else if(value >= 0.65 && value <= 1)
                                    return color[4];
                            }
                        })
                        .on("mouseover", function(d) {
                            d3.select(this).attr("fill","black");
                            div.transition()
                                .duration(200)
                                .style("opacity", .9);
                            div.html("Région : " + d.properties.nom + "<br>"
                                +  "Humeur : " + feeling(d.properties.value))
                                .style("left", (d3.event.pageX -350) + "px")
                                .style("top", (d3.event.pageY -200) + "px")
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
            <div id="map" ref="mapRender"></div>
        )
    }
}

export default Map;
