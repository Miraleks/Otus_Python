FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip && \
    pip install poetry==1.2.2

RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./

RUN poetry install --only main

COPY . .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0