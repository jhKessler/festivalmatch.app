import './Suggestions.css';
import FestivalmatchNavbar from './../../components/navbar/Navbar';
import Footer from './../../components/footer/Footer';
import { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import FestivalProgressbar from '../../components/progress_bar/FestivalProgressBar';
import FestivalDisplay from '../../components/festival_display/FestivalDisplay';
import { FestivalResponse } from '../../interfaces/FestivalResponse';
import SuccessAnimation from '../../components/success_animation/SuccessAnimation';

let progressInterval: any = null

function incrementProgress(progress: number, iters: number) {
    if (progress < 15) {
        return progress + 1
    } else if (iters < 40) {
        return progress
    }
    return progress + 2
}

function Suggestions() {
    useEffect(() => {
        document.title = "Your Festivals | festivalmatch.app"
      }, []);
    const [festivalReponse, setFestivalResponse] = useState<FestivalResponse>()
    const [progress, setProgress] = useState({
        iters: 0,
        progress: 0
    })

    const [animationDone, setAnimationDone] = useState(false)


    const [searchParams, _] = useSearchParams()
    const cookie = searchParams.get("code")
    
    useEffect(() => {
        fetch(`${process.env.REACT_APP_BACKEND_URL}/festivals?cookie=${cookie}`)
            .then(res => res.text())
            .then(data => setFestivalResponse(JSON.parse(data)))
    }, [])

    useEffect(() => {
        progressInterval = setInterval(() => {
            setProgress((prevProgress) => {
                return {
                    iters: prevProgress.iters + 1,
                    progress: incrementProgress(prevProgress.progress, prevProgress.iters)
                }
            })
        }, 75)
    }, [])

    useEffect(() => {
        if (progress.iters >= 100) {
            clearInterval(progressInterval)
        }
    }, [progress])


    let componentToShow = undefined
    if (progress.progress < 130) {
        componentToShow = FestivalProgressbar({ percentage: progress.progress })
    } else if (!animationDone) {
        componentToShow = SuccessAnimation({ setAnimationDone: setAnimationDone })
    } else {
        componentToShow = FestivalDisplay({ response: festivalReponse, isShared: false})
    }

    return (
        <div id="page-container">
            <div id="content-wrap">
                <FestivalmatchNavbar />
                {componentToShow}
            </div>
            <Footer />
        </div>
    );
}

export default Suggestions;
