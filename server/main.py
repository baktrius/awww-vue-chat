import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Vite's default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        clients.append(websocket)
        while True:
            data = await websocket.receive_text()
            for client in clients:
                await client.send_text(data)
    except WebSocketDisconnect:
        clients.remove(websocket)

@app.get("/slow")
async def slow():
    await asyncio.sleep(2)
    return "I'm slow"