from fastapi import FastAPI
import threading
from main import start_bot

app = FastAPI()

# Start the Discord bot in a separate thread
threading.Thread(target=start_bot, daemon=True).start()

@app.get("/")
async def root():
    return {"message": "Hello World, I'm Proggy Central's backend sever. I'm the helper, which keeps Proggy Central bot active all  the time without any issue or pain!"}

