from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI(
    title="ZeroTrust One",
    description="AI Powered Cybersecurity Platform",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "ZeroTrust One"
        }
    )


@app.get("/health")
async def health():
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "ZeroTrust One Backend"
        }
    )
