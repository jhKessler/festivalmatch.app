import FestivalmatchNavbar from './../../components/navbar/Navbar';
import Footer from './../../components/footer/Footer';
import './How.css';
import { useEffect } from 'react';

function How() {
  useEffect(() => {
    document.title = "How it works | festivalmatch.app"
  }, []);
  return (
    <div id="page-container">
      <div id="content-wrap">
        <FestivalmatchNavbar />
        <div className="main-content">
          <div className='how-start-buffer'></div>
            <span className="how-text-header">How it works</span>
            <div className="how-text">
              <span className="how-content-line">Finding good festivals is hard.</span>
              <br/>
              <span className="how-content-line">Using Spotify data to make accurate festival suggestions is even harder.</span>
              <br/>
              <div className="how-we-do-it-wrapper">
                <span className="how-text-medium">So how do we do it?</span>
              </div>
              <span className="how-content-line">All festivals in our database are given a similarity score based your Spotify Wrapped data.</span>
              <br/>
              <span className="how-content-line">
                By comparing the festivals with your listening habits, 
                your favorite artists and songs, <br/> and taking your rough geolocation into account,
                we can create a personalized list of festivals that you will enjoy.
              </span>
            </div>
          </div>
      </div>
      <Footer />
    </div>
  );
}

export default How;