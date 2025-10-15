"""Main application module."""

import os
from fastapi import FastAPI
from redis import Redis

app = FastAPI()

# Use str for environment variables; convert to int if needed
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.get("/")
def read_root():
    """Root endpoint returning a simple message."""
    return {"message": "Hello World"}