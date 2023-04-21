FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
WORKDIR /app/src
CMD uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8000
