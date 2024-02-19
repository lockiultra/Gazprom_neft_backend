FROM python:3.11-alpine

EXPOSE 8000
WORKDIR /app

RUN pip install --upgrade pip
RUN apk add --no-cache gcc musl-dev libffi-dev
RUN pip install poetry

COPY . /app

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-dev

CMD ["poetry", "run", "uvicorn", "main:app", "--port", "8000"]