export default function SyncGlowingEyesAvatar({ speaking }) {
  return (
    <>
      <style jsx>{`
        .eye {
          filter: drop-shadow(0 0 6px #00ffff);
          animation: ${speaking ? "pulseGlowSpeech 1s ease-in-out infinite alternate" : "pulseGlow 2s ease-in-out infinite alternate"};
          transform-origin: center;
        }
        #eye-left {
          animation-delay: 0s;
        }
        #eye-right {
          animation-delay: 0.5s;
        }

        @keyframes pulseGlow {
          0% {
            fill: #00ffff;
            filter: drop-shadow(0 0 4px #00ffffaa);
            transform: scale(1);
            opacity: 1;
          }
          50% {
            fill: #7f00ff;
            filter: drop-shadow(0 0 12px #7f00ffaa);
            transform: scale(1.15);
            opacity: 0.8;
          }
          100% {
            fill: #00ffff;
            filter: drop-shadow(0 0 4px #00ffffaa);
            transform: scale(1);
            opacity: 1;
          }
        }

        @keyframes pulseGlowSpeech {
          0%, 100% {
            fill: #00ffff;
            filter: drop-shadow(0 0 20px #00ffffff);
            transform: scale(1.2);
            opacity: 1;
          }
          50% {
            fill: #7f00ff;
            filter: drop-shadow(0 0 28px #7f00ffff);
            transform: scale(1.4);
            opacity: 0.9;
          }
        }
      `}</style>

      <svg
        viewBox="0 0 100 100"
        xmlns="http://www.w3.org/2000/svg"
        width="120"
        height="120"
        role="img"
        aria-label="Alien avatar with glowing eyes"
      >
        <circle cx="50" cy="50" r="45" fill="#0a0a0a" stroke="#00ffff" strokeWidth="3" />
        <circle id="eye-left" className="eye" cx="30" cy="40" r="8" />
        <circle id="eye-right" className="eye" cx="70" cy="40" r="8" />
      </svg>
    </>
  );
}
