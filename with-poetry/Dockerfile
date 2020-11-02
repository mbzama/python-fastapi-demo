
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./ /app

RUN python -m pip install --upgrade pip

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install