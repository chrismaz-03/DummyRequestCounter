from dotenv import load_dotenv
import os
from redis import Redis
from fastapi import FastAPI

# Load environment variables from .env
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Redis configuration
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

# Connect to Redis
redis = Redis(host=redis_host, port=redis_port)

@app.get("/")
def hello():
    # Increment a counter in Redis
    try:
        redis.incr("hits")
    except Exception:
        pass  # ignore Redis errors during testing
    return {"message": "Hello World"}
