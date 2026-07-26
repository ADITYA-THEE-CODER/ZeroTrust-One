from urllib.parse import urlparse
import ipaddress


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "bank",
    "wallet",
    "crypto",
    "gift",
    "paypal",
    "invoice",
    "password",
]


SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "rb.gy",
]


def analyze_url(url: str):

    score = 0
    checks = []

    parsed = urlparse(url)

    if not parsed.scheme:
        return {
            "url": url,
            "risk_score": 100,
            "threat": "INVALID",
            "checks": ["Invalid URL"],
            "recommendation": "Enter a valid URL."
        }

    if parsed.scheme == "http":
        score += 25
        checks.append("Uses HTTP instead of HTTPS")

    domain = parsed.netloc.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in url.lower():
            score += 10
            checks.append(f"Contains '{keyword}'")

    for shortener in SHORTENERS:
        if shortener in domain:
            score += 20
            checks.append("Uses URL shortener")

    try:
        ipaddress.ip_address(domain)
        score += 30
        checks.append("Uses IP address instead of domain")
    except:
        pass

    if domain.endswith(".xyz"):
        score += 20
        checks.append("Suspicious TLD (.xyz)")

    if score >= 70:
        threat = "HIGH"
    elif score >= 40:
        threat = "MEDIUM"
    else:
        threat = "LOW"

    recommendation = (
        "Avoid opening this URL."
        if threat == "HIGH"
        else "Exercise caution."
        if threat == "MEDIUM"
        else "No major issues detected."
    )

    return {
        "url": url,
        "risk_score": min(score, 100),
        "threat": threat,
        "checks": checks,
        "recommendation": recommendation,
    }
