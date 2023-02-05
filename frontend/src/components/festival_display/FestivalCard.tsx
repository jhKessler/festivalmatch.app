import { Festival } from "../../interfaces/Festival";
import "./FestivalCard.css";
import SpotifyLogo from "../../assets/SpotifyLogoWhite.png";

function splitLineup(lineup: string[]) {
    let rowSizes = [1, 3, 11]
    let lineupRows = []

    for (let i = 0; i < rowSizes.length; i++) {
        let lineupRow = lineup.slice(0, rowSizes[i])
        if (lineupRow.length > 1) {
            for (let i=0; i < lineupRow.length; i++) {
                if (i < (lineupRow.length-1)) {
                    lineupRow[i] = lineupRow[i] + ", "
                }
            }
        }


        lineupRows.push(lineupRow)
        lineup = lineup.slice(rowSizes[i])
    }
    return lineupRows
}


function FestivalCard(props: {festival: Festival}) {
    const lineupRows = splitLineup(props.festival.lineup)
    return (
        <div className="festival-card">
            <div className="festival-card-content">
                <div className="festival-link">
                    <a className="festival-card-title" target="_blank" rel="noopener noreferrer" href={props.festival.website}>{props.festival.name}</a>
                </div>
                <p className="festival-card-date">{props.festival.date}</p>
                <p className="festival-card-location">{props.festival.location}</p>
                <p className="festival-headliner"><span className="lineup-artist">{lineupRows[0][0]}</span></p>
                <p className="festival-second-row">{lineupRows[1].map((element) => <span className="lineup-artist">{element}</span>)}</p>
                <p className="festival-third-row">{lineupRows[2].map((element) => <span className="lineup-artist">{element}</span>)}</p>
            </div>
                <div className="powered-by-spotify">
                    <p className="powered-by-spotify-text">Powered by</p>
                    <div className="powered-by-row">
                        <div className="powered-by-spotify-logo-wrapper">
                            <img className="powered-by-spotify-logo" src={SpotifyLogo} alt="Spotify Logo"/>
                        </div>
                        <div className="powered-by-festivalmatch-logo-wrapper">
                            <div className="powered-by-festivalmatch-logo">
                                <span className="powered-by-festivalmatch-logo-name">festivalmatch</span>
                                <span className="powered-by-festivalmatch-logo-domain">.app</span>
                            </div>
                        </div>
                        
                    </div>
                </div>
        </div>
    )
}

export default FestivalCard;