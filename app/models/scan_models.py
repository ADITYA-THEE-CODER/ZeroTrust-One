from pydantic import BaseModel


class URLScanRequest(BaseModel):
    url: str


class URLScanResponse(BaseModel):
    url: str
    risk_score: int
    threat: str
    checks: list[str]
    recommendation: str
