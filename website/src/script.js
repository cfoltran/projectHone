
var width = 900, height = 900;

var path = d3.geoPath();

var projection = d3.geoConicConformal()
    .center([2.454071, 46.379229])
    .scale(4000)
    .translate([width / 2, height / 2]);

path.projection(projection);

var svgMap = d3.select('#map').append("svg")
    .attr("id", "svg")
    .attr("width", width)
    .attr("height", height);

var deps = svgMap.append("g");


var div = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

var lol=null
var i= 1

d3.json('departments.json', function(req, geojson) {
    test=geojson

    deps.selectAll("path")
        .data(geojson.features)
        .enter()
        .append("path")
        .attr('class', 'department')
        .attr("d", path)
        .attr("fill","rgba(98,225,230,0.5)")
        .attr("stroke","black")

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
});