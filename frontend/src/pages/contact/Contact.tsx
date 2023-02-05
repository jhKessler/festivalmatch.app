import './Contact.css';
import FestivalmatchNavbar from './../../components/navbar/Navbar';
import Footer from './../../components/footer/Footer';
import { useEffect } from 'react';

function Contact() {
  useEffect(() => {
    document.title = "Contact | festivalmatch.app"
  }, []);
  return (
    <div id="page-container">
      <div id="content-wrap">
        <FestivalmatchNavbar />
        <div className="main-content">
        <div className='contact-start-buffer'></div>
        <div className="contact-text-header">Contact</div>
            <p className="contact-text-line">Johnny Kessler</p>
            <p className="contact-text-line">johnnyhagenkessler@gmail.com</p>
            <p className="contact-text-line">Bruchloh 26, 22589 Hamburg</p>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Contact;
