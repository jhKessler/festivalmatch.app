import { Link } from "react-router-dom";
import "./Footer.css"

function Footer() {
    return (
        <div className="mainfooter">
            <div className="legal-text footer-text">
                festivalmatch.app is not affiliated with Spotify or any of the festivals listed on this website.
            </div>
            <div className="footer-link-wrapper">
                <Link className="footer-text footer-link" to="/">festivalmatch.app</Link>
                <Link className="footer-text footer-link" to="/how">How it works</Link>
                <Link className="footer-text footer-link" to="/contact">Contact</Link>
                <Link className="footer-text footer-link" to="/privacy">Privacy</Link>
            </div>
        </div>
    );
}

export default Footer;