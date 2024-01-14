FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ROOT /edu

WORKDIR ${ROOT}
COPY pyproject.toml ${ROOT}

RUN pip3 install --upgrade pip && pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi