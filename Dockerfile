FROM python:3.11-alpine

EXPOSE 8000
WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ['uvicorn', 'main:app', '--port', '8000']