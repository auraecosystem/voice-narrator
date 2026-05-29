# services/realtime/main.py

from fastapi import FastAPI, WebSocket
import asyncio
import json

app = FastAPI()

clients = []

@app.websocket("/realtime")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            data = await websocket.receive_bytes()

            # audio chunk received
            transcript = await process_audio(data)

            response = await agent_response(transcript)

            audio_reply = await synthesize_voice(response)

            await websocket.send_json({
                "transcript": transcript,
                "response": response
            })

            await websocket.send_bytes(audio_reply)

    except Exception as e:
        print(e)

    finally:
        clients.remove(websocket)


async def process_audio(audio_bytes):
    # whisper inference
    return "Hello from QUBUHUB"


async def agent_response(text):
    # GPT / local model inference
    return f"Narrator response to: {text}"


async def synthesize_voice(text):
    # XTTS / Kokoro generation
    return b"audio-bytes"
