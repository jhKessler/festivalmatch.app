import "./FestivalCarousel.css";

import { Festival } from "../../interfaces/Festival";

import FestivalCard from "./FestivalCard";
import { Carousel } from 'react-responsive-carousel';
import { useState, useRef } from "react";
import "react-responsive-carousel/lib/styles/carousel.min.css"
import html2canvas from 'html2canvas';
import ShareButtons from "../share_buttons/ShareButtons";
import { FestivalResponse } from "../../interfaces/FestivalResponse";


async function downloadFestivalCard(festivalCard: any, festivalName: string) {
    const canvas = await html2canvas(festivalCard, {backgroundColor: "black"})
    const data = canvas.toDataURL('image/png')
    const link = document.createElement('a')

    if (typeof link.download === 'string') {
        link.href = data
        link.download = `${festivalName.trim().replaceAll(" ", "-")}-festivalmatch.png`
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
    } else {
        window.open(data)
    }

}

function FestivalCarousel(props: { response: FestivalResponse, isShared: boolean }) {
    let festivals: Festival[] = props.response.suggestions
    let hash = props.response.hash
    const [carouselIndex, setCarouselIndex] = useState(0)
    const festivalRefs = [useRef(), useRef(), useRef(), useRef(), useRef()]
    return (
        <>
        <Carousel
                infiniteLoop={true} 
                showStatus={false} 
                swipeScrollTolerance={35}
                showThumbs={false}
                showIndicators={false}
                className="carousel-fest"
                onChange={(index) => setCarouselIndex(index)}
        >
            {festivals.map((festival, index) => (
                // @ts-ignore
                <div ref={festivalRefs[index]} key={index}><FestivalCard festival={festival}/></div>
            ))}
        </Carousel>
        {props.isShared? null : ShareButtons({ hash: hash})}
        {props.isShared? null : <button className="download-button" onClick={() => {
            downloadFestivalCard(festivalRefs[carouselIndex].current, festivals[carouselIndex].name)
        }}>Download Image</button>}
        
        </>  
    )
}

export default FestivalCarousel;