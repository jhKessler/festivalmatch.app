import './Shared.css';
import FestivalmatchNavbar from './../../components/navbar/Navbar';
import Footer from './../../components/footer/Footer';
import { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import FestivalDisplay from '../../components/festival_display/FestivalDisplay';
import { FestivalResponse } from '../../interfaces/FestivalResponse';


function Suggestions() {
    useEffect(() => {
        document.title = "Shared Festivals | festivalmatch.app"
      }, []);
    const [festivalReponse, setFestivalResponse] = useState<FestivalResponse>()
    const [searchParams, _] = useSearchParams()
    const hash = searchParams.get("hash")
    
    useEffect(() => {
        fetch(`${process.env.REACT_APP_BACKEND_URL}/shared?hash=${hash}`)
            .then(res => res.text())
            .then(data => {
                let parsed = JSON.parse(data)
                setFestivalResponse(parsed)
            })
    }, [])

    return (
        <div id="page-container">
            <div id="content-wrap">
                <FestivalmatchNavbar />
                {festivalReponse == null? null : FestivalDisplay({ response: festivalReponse, isShared: true })}
            </div>
            <Footer />
        </div>
    );
}

export default Suggestions;
