from fastapi import FastAPI, Response, status

app = FastAPI(title="platform-api", version="0.1.0")

_ready = True


@app.get("/")
def root():
    return {"service": "platform-api", "version": "0.1.0"}


@app.get("/healthz")
def healthz():
    """Liveness: process is up."""
    return {"status": "ok"}


@app.get("/readyz")
def readyz(response: Response):
    """Readiness: safe to receive traffic."""
    if not _ready:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "not ready"}
    return {"status": "ready"}
