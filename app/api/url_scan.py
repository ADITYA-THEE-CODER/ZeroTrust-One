from fastapi import APIRouter

from app.models.scan_models import URLScanRequest
from app.scanners.url_scanner import analyze_url

router = APIRouter()


@router.post("/scan/url")
async def scan_url(request: URLScanRequest):

    return analyze_url(request.url)
