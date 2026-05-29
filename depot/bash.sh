# backend
cd services/realtime
uvicorn main:app --reload --host 0.0.0.0 --port 8000
cd apps/web
npm install
npm run dev
cd apps/desktop
npm install
electron .
pip install fastapi uvicorn websockets openai-whisper torch TTS qdrant-client redis asyncpg
pip install onnxruntime-gpu tensorrt

# services/
 ├── realtime/
 ├── orchestration/
 ├── emotion-engine/
 ├── narrator-core/
 ├── memory/
 ├── vector-search/
 ├── vision/
 ├── automation/
 └── voice-cloning/
