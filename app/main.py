from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.url_scan import router as url_router

app = FastAPI(
    title="ZeroTrust One",
    description="AI-Powered Cybersecurity Platform",
    version="1.0.0"
)

# Register API routes
app.include_router(url_router, prefix="/api", tags=["URL Scanner"])

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "ZeroTrust One"
        }
    )


@app.get("/health")
async def health():
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "ZeroTrust One Backend",
            "version": "1.0.0"
        }
    )
