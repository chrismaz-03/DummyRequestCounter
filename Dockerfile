FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

WORKDIR /app/app

ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]