import { useState } from "react"
import "./CopyButton.css"
import {ReactComponent as CopyLinkIcon} from "./../../assets/popup-link-icon.svg";


function CopyButton(props: { hash: string }) {
    const [copied, setCopied] = useState(false)
    return (
        <div className="share-icon-wrapper">
            <CopyLinkIcon className="copy-button-icon" onClick={() => setCopied(true)}/>
        </div>
    )
}

export default CopyButton;