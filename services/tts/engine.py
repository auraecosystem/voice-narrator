# services/tts/engine.py

from TTS.api import TTS

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

async def generate(text):
    path = "output.wav"

    tts.tts_to_file(
        text=text,
        file_path=path
    )

    with open(path, "rb") as f:
        return f.read()
