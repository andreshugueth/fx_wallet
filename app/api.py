from fastapi import FastAPI


app = FastAPI(
    title="FX Wallet API",
    description="A simple API to manage a multi-currency wallet with real-time exchange rates.",
    version="1.0.0",
)


@app.get("/ping/", tags=["Health Check"])
async def ping():
    return {"message": "pong"}
