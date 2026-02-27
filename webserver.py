# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later

#imort fastapi
from fastapi import FastAPI
import threading #for running the main file alongside with this
from main import start_bot #a function which runs the bot

app = FastAPI()

# Start the Discord bot in a separate thread
@app.on_event("startup")
async def startup_event():
    threading.Thread(target=start_bot, daemon=True).start()

@app.get("/") #if user visited the root
async def root():
    return {"message": "Hello World, I'm Proggy Central's backend sever. I'm the helper, which keeps Proggy Central bot active all  the time without any issue or pain!"}

