FROM python:3.11-slim
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . .
ENV TZ="Europe/Moscow"
CMD poetry run python src/