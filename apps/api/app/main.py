from fastapi import FastAPI

app = FastAPI(title="platform-api", version="0.1.0")


@app.get("/")
def root():
    return {"service": "platform-api", "version": "0.1.0"}
