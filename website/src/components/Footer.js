
import React from 'react';
import { Col, Container, Row, Footer } from 'mdbreact';

class FooterPage extends React.Component {
    render(){
        return(
            <Footer color="unique-color-dark" className="page-footer font-small pt-0">
                <div style={{backgroundColor: '#6351ce'}}>
                    <Container className="text-left">
                        <Row className="py-4 d-flex align-items-center">
                            <Col md="6" lg="5" className="text-center text-md-left mb-4 mb-md-0">
                                <h6 className="mb-0 white-text font-30">Restez connecté sur nos reseaux!</h6>
                            </Col>
                            <Col md="6" lg="7" className="text-center text-md-right">
                                <a className="fb-ic ml-0 font-30"><i className="fa fa-facebook white-text mr-lg-4"> </i></a>
                                <a className="tw-ic font-30"><i className="fa fa-twitter white-text mr-lg-4"> </i></a>
                                <a className="gplus-ic font-30"><i className="fa fa-google-plus white-text mr-lg-4"> </i></a>
                                <a className="li-ic font-30"><i className="fa fa-linkedin white-text mr-lg-4"> </i></a>
                                <a className="ins-ic font-30"><i className="fa fa-instagram white-text mr-lg-4"> </i></a>
                            </Col>
                        </Row>
                    </Container>
                </div>
                <Container className="mt-5 mb-4 text-center text-md-left">
                    <Row className="mt-3">
                        <Col md="3" lg="4" xl="3" className="mb-4">
                            <h6 className="text-uppercase font-weight-bold"><strong>Company name</strong></h6>
                            <hr className="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: '60px'}}/>
                            <p> Lorem ipsum dolor sit
                                amet, consectetur adipisicing elit.Lorem ipsum dolor sit
                                amet, consectetur adipisicing elit.</p>
                        </Col>
                        <Col md="2" lg="2" xl="2" className="mb-4">
                            <h6 className="text-uppercase font-weight-bold"><strong>lorem</strong></h6>
                            <hr className="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: '60px'}}/>
                            <p><a href="#!">lorem</a></p>
                            <p><a href="#!">lorem</a></p>
                            <p><a href="#!">lorem</a></p>
                            <p><a href="#!">lorem lorem</a></p>
                        </Col>
                        <Col md="3" lg="2" xl="2" className="mb-4">
                            <h6 className="text-uppercase font-weight-bold"><strong>lorem lorem</strong></h6>
                            <hr className="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: '60px'}}/>
                            <p><a href="#!">lorem lorem</a></p>
                            <p><a href="#!">lorem lorem</a></p>
                            <p><a href="#!">lorem lorem</a></p>
                            <p><a href="#!">lorem</a></p>
                        </Col>
                        <Col md="4" lg="3" xl="3" className="mb-4">
                            <h6 className="text-uppercase font-weight-bold"><strong>Contact</strong></h6>
                            <hr className="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: '60px'}}/>
                            <p><i className="fa fa-home mr-3"></i>IUT ORSAY</p>
                            <p><i className="fa fa-envelope mr-3"></i> promo-4h@u-psud.fr</p>
                            <p><i className="fa fa-phone mr-3"></i> + 01 234 567 88</p>
                            <p><i className="fa fa-print mr-3"></i> + 01 234 567 89</p>
                        </Col>
                    </Row>
                </Container>
                <div className="footer-copyright text-center">
                    <Container fluid>
                        &copy; {(new Date().getFullYear())} Copyright: <a href="/">JOAnalytweet.com </a>
                    </Container>
                </div>
            </Footer>
        );
    }
}

export default FooterPage;
