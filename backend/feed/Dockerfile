FROM python:3.11

COPY . .

RUN pip install -r requirements.txt

RUN uvicorn main:feed_service --reload --host 0.0.0.0 --port 8000