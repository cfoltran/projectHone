//todo collect input value from searchBar.js
import React from 'react';

import Searchbar from './Searchbar';
import DashBoard from "./DashBoard"
import BarChart from './BarChart';


class Search extends React.Component{


    render(){
        // const tag = Object.keys(this.state.tagSementic).map(key => <Searchbar key={key} details={this.state.tagSementic[key]}/>);
        return (
            <div>

                <Searchbar/>
                {/*--------------------------------*/}
                {/*----------Get the search--------*/}
                {/*--------------------------------*/}
                <section className="bg-white text-center">
                    <div className="container">
                        <h2 className="font-60 text-dark">Recherche:</h2>
                        <div className="row text-center">
                            <div className="col-md-12  padding-150">
                                 <p className="text-dark"> Vous avez recherchez: {this.props.match.params.tag} <br/>
                        Avec le sentiment: {this.props.match.params.sementic}
                        {/*Todo get the sementic*/}
                                </p>
                            </div>

                        </div>
                    </div>
                </section>

                {/*--------------------------------*/}
                {/*----------Dash Board------------*/}
                {/*--------------------------------*/}
                <section className="bg-dark">
                    <div className="container">
                        <h2 className="font-60 text-center text-cloud">Dash Board :</h2>
                        <div className="row">
                    <DashBoard/>
                        </div>
                    </div>
                </section>

                {/*--------------------------------*/}
                {/*-----------Bar Chart------------*/}
                {/*--------------------------------*/}
                <div>
                    <div className="bg-white">
                        <h2 className="font-60 text-center">Bar chart:</h2>
                            <div className="container">
                                <div className="row">
                                    <BarChart/>
                                </div>
                            </div>
                    </div>
                </div>
            </div>
        )
    }

}


export default Search;