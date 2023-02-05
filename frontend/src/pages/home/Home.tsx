import './Home.css';
import FestivalmatchNavbar from './../../components/navbar/Navbar';
import Footer from './../../components/footer/Footer';
import GetStartedButton from '../../components/get_started_button/GetStartedButton';
import { Link } from 'react-router-dom';
import { useEffect } from 'react';

function Home() {
  useEffect(() => {
    document.title = "Festivalmatch - Find your perfect festival using your Spotify history"
  }, []);
  return (
    <div id="page-container">
      <div id="content-wrap">
        <FestivalmatchNavbar />
        <div className="main-content">
          <div className='home-start-buffer'></div>
          <span className="home-text-small">Want to find interesting festivals that suit your taste in music?</span>
          <span className="home-text-big">You're at the right place!</span>
          <span className="home-text-small">
            festivalmatch uses your <a href="https://www.spotify.com/us/wrapped/" target="_blank" rel="noopener noreferrer" className='purple-href'>Spotify Wrapped</a> to find festivals that you might like.
            <br />
            Sign in with your Spotify account to get started!
          </span>
          <GetStartedButton />
          <span className="home-text-small">
            Curious how we match you with festivals?
            <br/>
            Click <Link to="/how" className="purple-href">here</Link> to find out how it works!
          </span>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Home;
