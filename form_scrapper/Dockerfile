FROM python:3.10-slim
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
COPY . .
CMD ["uvicorn", "form_scrapper.server.app:app", "--host", "0.0.0.0", "--port", "8000"]
