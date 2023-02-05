import {
    WhatsappShareButton, WhatsappIcon,
    TwitterShareButton, TwitterIcon,
    RedditShareButton, RedditIcon,
    TelegramShareButton, TelegramIcon,
    
} from "react-share";
import CopyButton from "../copy_link_button/CopyButton";
import { FestivalResponse } from "../../interfaces/FestivalResponse";
import "./ShareButtons.css"


function ShareButtons(props: { hash: string }) {
    let shareText = "I just got my personalized festival recommendations from Festivalmatch! Try it out as well:"
    let shareURL = `https://festivalmatch.app/shared?hash=${props.hash}`
    return <div className="share-items">
        <span className="share-text">Share festivals</span>
        <div className="share-buttons">
            <WhatsappShareButton url={shareURL} title={shareText} className="share-button">
                <WhatsappIcon round={true} className="share-icon"/>
            </WhatsappShareButton>
            <TwitterShareButton url={`${shareURL}`} title={shareText} className="share-button">
                <TwitterIcon round={true} className="share-icon"/>
            </TwitterShareButton>
            <RedditShareButton url={`${shareURL}`} title={shareText} className="share-button">
                <RedditIcon round={true} className="share-icon"/>
            </RedditShareButton>
            <TelegramShareButton url={`${shareURL}`} title={shareText} className="share-button">
                <TelegramIcon round={true} className="share-icon"/>
            </TelegramShareButton>
        </div>
    </div>
}

export default ShareButtons;