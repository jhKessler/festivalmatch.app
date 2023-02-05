import './Privacy.css';
import FestivalmatchNavbar from './../../components/navbar/Navbar';
import Footer from './../../components/footer/Footer';
import { Link } from 'react-router-dom';
import { useEffect } from 'react';

function Privacy() {
  useEffect(() => {
    document.title = "Privacy | festivalmatch.app"
  }, []);
  return (
    <div id="page-container">
      <div id="content-wrap">
        <FestivalmatchNavbar />
        <div className="main-content">
        <div className='privacy-start-buffer'></div>
            <span className="privacy-text-header">Privacy Policy</span>
            <span className="privacy-text-line">Festivalmatch uses the Spotify Web API to get data from your Spotify profile.</span>
            <span className="privacy-text-line">When you log in to festivalmatch, we will ask you to grant us access to your Spotify profile.</span>
            <span className="privacy-text-line">This access also includes your top artists and top songs.</span>
            <span className="privacy-text-line">We will use this data to give you personalized festival suggestions.</span>
            <span className="privacy-text-line">Your top artists and tracks are stored anonymously on our servers for the purposes of improving our festival suggestions in the future.</span>
            <span className="privacy-text-line">We will not share your data with any third parties.</span>
            <span className="privacy-text-line">Anonymized usage data is stored to improve the usability of our website, this data is not connected to your identity and is only used for optimizing the website design.</span>
            <span className="privacy-text-line">By using festivalmatch, you agree to the terms of this privacy policy.</span>
            <span className="privacy-text-line">If at any point you wish to remove Festivalmatch's permissions on Spotify, you can do so 
                <a className="purple-href-privacy" target="_blank" rel="noopener noreferrer" href="https://support.spotify.com/us/article/spotify-on-other-apps/"> here</a>.
            </span>
            <span className="privacy-text-line">For any questions, feel free to <Link className="purple-href-privacy" to="/contact">contact us</Link>.</span>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Privacy;
