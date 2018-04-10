//todo collect input value from searchBar.js
import React from 'react';

import DashBoard from "./DashBoard"
import BarChart from './BarChart';
import NavbarFeatures from "./NavbarFeatures";
import FooterPage from "./Footer";



class Search extends React.Component{

  constructor(props) {
     super(props);
     this.state = {
       tag: this.props.match.params.tag,
     };
   }

    render(){
        // const tag = Object.keys(this.state.tagSementic).map(key => <Searchbar key={key} details={this.state.tagSementic[key]}/>);
        return (
            <div>

                <NavbarFeatures/>
                {/*--------------------------------*/}
                {/*----------Get the search--------*/}
                {/*--------------------------------*/}
                <section className="bg-white text-center">
                    <div className="container">
                        <h2 className="font-70 text-dark">Recherche:</h2>
                        <div className="row text-center">
                            <div className="col-md-12  padding-150">
                                <p className="text-dark font-40"> Vous avez recherchez: {this.state.tag} <br/>
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
                        <h2 className="font-70 text-center text-cloud">Dash Board :</h2>
                        <div className="row">
                            <DashBoard/>
                        </div>
                    </div>
                </section>

                {/*--------------------------------*/}
                {/*-----------Bar Chart------------*/}
                {/*--------------------------------*/}
                <div>
                    <section className="bg-white">
                        <div className="container">
                            <h2 className="font-70 text-center padding-10">Bar chart:</h2>
                            <div className="row">
                                <BarChart props={this.state.tag}/>
                            </div>
                        </div>
                    </section >
                </div>
                <FooterPage/>
            </div>


        )
    }

}


export default Search;
