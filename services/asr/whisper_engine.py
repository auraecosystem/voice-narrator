# services/asr/whisper_engine.py

import whisper

model = whisper.load_model("base")

async def transcribe(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
