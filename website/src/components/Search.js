//todo collect input value from searchBar.js
import React from 'react';

import Searchbar from './NavbarSearch';
import DashBoard from "./DashBoard";
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
                <section className="bg-dark text-center">
                    <div className="container">
                        <h2 className="font-60">Recherche:</h2>
                        <div className="row text-center">
                            <div className="col-md-12  padding-150">
                                 <p className="text-cloud"> Vous avez recherchez: {this.props.match.params.tag} <br/>
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
                <section>
                    <div className="container">
                        <h2 className="font-60 text-center">Dash Board :</h2>
                        <div className="row">
                    <DashBoard/>
                        </div>
                    </div>
                </section>

                {/*--------------------------------*/}
                {/*-----------Bar Chart------------*/}
                {/*--------------------------------*/}
                <section className="bg-dark">
                    <div className="container">
                        <h2 className="font-60 text-center padding-150">Bar chart</h2>
                        <div className="row">
                            <BarChart/>
                        </div>
                    </div>
                </section>
            </div>
        )
    }

}


export default Search;