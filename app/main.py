from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

app = FastAPI(
    title="ZeroTrust One",
    description="AI Powered Cybersecurity Platform",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def root():
    return {
        "name": "ZeroTrust One",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "ZeroTrust One Backend"
        }
    )
