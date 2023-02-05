import "./GetStartedButton.css"
import SpotifyWhite from "./../../assets/SpotifyWhite.png" 
import { Link } from "react-router-dom";

function GetStartedButton() {
    return (
        <a className="get-started-button" href={`${process.env.REACT_APP_BACKEND_URL}/login`}>
            <img src={SpotifyWhite} className="get-started-button-logo"/>
            Get Started With Spotify
        </a>
    )
}

export default GetStartedButton;