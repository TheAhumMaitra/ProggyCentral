from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World, I'm Proggy Central's backend sever. I'm the helper, which keeps Proggy Central bot active all  the time without any issue or pain!"}
