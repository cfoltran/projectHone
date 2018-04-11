import React, { Component } from 'react';
import * as d3 from 'd3';
import '../style/css/DashBoard.css';

class DashBoard extends Component {

  constructor(props) {
     super(props);
     this.state = {
       tag: this.props,
     };
     //get the hash do this.state.tag
   }

   componentDidMount() {
        this.initDashboard(this.state.tag)
    }

    componentDidUpdate(){
        this.initDashboard(this.state.tag)
    }
    initDashboard(tag){
            var ppc = d3.select('.progress-pie-chart'),
            percent = parseInt(ppc.data('percent'),10),
            deg = 360*percent/100;
          if (percent > 50) {
            ppc.addClass('gt-50');
          }
          d3.select('.ppc-progress-fill').style('transform','rotate('+ deg +'deg)');
          d3.select('.ppc-percents span').html(percent+'%');

            d3.json("http://localhost:5001/statistics/hashtag/"+tag, function(data) {
             
              d3.select('#tweet').html(data.statistics['0'].NumbersOfTweets);
              d3.select('#rt').html(data.statistics['0'].AverageRetweets);
 				d3.select('#humeur').html(data.statistics['0'].AveragePolarity);
            
        });
    }
  render() {
    return (
           <div className="progressDiv">
            <div className="statChartHolder">
                {/*Pie Chart*/}
                <div className="progress-pie-chart" >
                    <div className="ppc-progress">
                        <div className="ppc-progress-fill"></div>
                    </div>
                    <div className="ppc-percents">
                    <div className="pcc-percents-wrapper">
                        <span> %</span>
                    </div>
                    </div>
                </div>
                {/*End Chart*/}
            </div>
            <div className="statRightHolder">

                <ul>
                    <li> <h3><span>Nombre de Tweet</span></h3> <div id='tweet' className="font-30"/>
                  </li>
                    <li> <h3><span>Nombre de RT moyen</span></h3> <div id='rt' className="font-30"/> </li>
					<li> <h3><span>Humeur</span></h3> <div id='humeur' className="font-30"/> </li>
                </ul>

                    
            </div>

        </div>
    );
  }
}

export default DashBoard;

