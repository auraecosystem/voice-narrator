import { useEffect, useRef, useState } from "react";

export default function AITTSPlayer({ text, onStart, onEnd }) {
  const audioRef = useRef(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!text) return;

    setLoading(true);

    fetch("/api/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    })
      .then((res) => res.arrayBuffer())
      .then((buffer) => {
        const blob = new Blob([buffer], { type: "audio/mpeg" });
        const url = URL.createObjectURL(blob);
        audioRef.current.src = url;
        audioRef.current.play();
        onStart && onStart();
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [text, onStart]);

  return (
    <>
      <audio
        ref={audioRef}
        onEnded={() => onEnd && onEnd()}
        onPause={() => onEnd && onEnd()}
        hidden
      />
      {loading && <div style={{ color: "#0ff" }}>Loading voice...</div>}
    </>
  );
}
