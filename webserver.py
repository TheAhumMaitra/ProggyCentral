# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later

import threading
from contextlib import asynccontextmanager

from fastapi import FastAPI

from main import start_bot


@asynccontextmanager
async def lifespan(app: FastAPI):
    threading.Thread(target=start_bot, daemon=True).start()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {
        "message": "Hello World, I'm Proggy Central's backend sever. I'm the helper, which keeps Proggy Central bot active all  the time without any issue or pain!"
    }
