// apps/web/lib/microphone.ts

export async function startMicrophone(ws: WebSocket) {
  const stream = await navigator.mediaDevices.getUserMedia({
    audio: true
  })

  const mediaRecorder = new MediaRecorder(stream)

  mediaRecorder.ondataavailable = async (event) => {
    const buffer = await event.data.arrayBuffer()
    ws.send(buffer)
  }

  mediaRecorder.start(250)
}
