import ProgressBar from 'react-bootstrap/ProgressBar';
import "./FestivalProgressBar.css"


function getUpdateText(percentage: number) {
    if (percentage <= 15) {
        return "Talking to Spotify..."
    } else if (percentage < 65) {
        return "Analyzing your music taste..."
    } else if (percentage < 100) {
        return "Matching you with festivals..."
    } else {
        return "Almost there!"
    }
}


function FestivalProgressbar(props: {percentage: number}) {
    return (
        <>
        <div className='progressbar-buffer'></div>
        <div className='progressBarWrapper'>
            <span className='almost-there'>Almost there!</span>
            <br/>
            <span className='progress-text'>We are creating your personalized suggestions right now.</span>
            <ProgressBar animated now={props.percentage} variant="loadingBar"/>
            <span className='status-text'>{getUpdateText(props.percentage)}</span>
        </div>
        </>
    );
}

export default FestivalProgressbar;
