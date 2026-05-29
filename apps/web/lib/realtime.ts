// apps/web/lib/realtime.ts

const ws = new WebSocket("ws://localhost:8000/realtime")

ws.onopen = () => {
  console.log("Connected to narrator")
}

ws.onmessage = async (event) => {
  if (typeof event.data === "string") {
    const data = JSON.parse(event.data)

    console.log(data.transcript)
    console.log(data.response)
  } else {
    const audioBlob = new Blob([event.data], {
      type: "audio/wav"
    })

    const audio = new Audio(URL.createObjectURL(audioBlob))
    audio.play()
  }
}

export default ws
