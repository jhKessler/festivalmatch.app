import Lottie from "lottie-react";
import successAnimation from "./../../assets/successAnimation.json";
import './SuccessAnimation.css';

function SuccessAnimation(props: { setAnimationDone: (animationDone: boolean) => void }) {
      return (
        <div className="success-animation">
            <Lottie animationData={successAnimation} loop={false} onComplete={(anim) => props.setAnimationDone(true)}/>
        </div>
      )
}

export default SuccessAnimation;
