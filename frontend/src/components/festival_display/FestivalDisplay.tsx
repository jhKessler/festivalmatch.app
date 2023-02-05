import './FestivalDisplay.css';
import { FestivalResponse } from '../../interfaces/FestivalResponse';
import FadeIn from 'react-fade-in';
import FestivalCarousel from './FestivalCarousel';
import ShareButtons from '../share_buttons/ShareButtons';


function isValidResponse(response: FestivalResponse | undefined): boolean {
    return response?.status === "success" && response?.suggestions.length > 0
}

function FestivalDisplay(props: { response: FestivalResponse | undefined , isShared: boolean}) {
    if (!isValidResponse(props.response)) {
        return (
            <div className='error-page'>
                <div className="error-buffer"></div>
                Something went wrong. This may be due to a bug in our system, or there may be no festivals that match your taste in music at this time.
                <br/>
                Please try again later! We are always working on improving our system.
            </div>
        )
    }
    return (
        <FadeIn>
            <div className="festival-display">
                <div className='festival-display-buffer'></div>
                <div className="festival-display-user-greeting">
                    <span className="user-greeting-text">{props.isShared? "Shared Festivals" : `Festivals for ${props.response?.username}`}</span>
                </div>
                <FestivalCarousel response={props.response!} isShared={props.isShared}/>
            </div>
        </FadeIn>
    )
}

export default FestivalDisplay;
