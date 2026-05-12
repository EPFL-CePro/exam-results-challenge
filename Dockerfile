FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy the project files, without files specified in .dockerignore (venv, ide files, test coverage files, etc.)
COPY . .

# Install the project with production dependencies
RUN pip install --no-cache-dir ".[prod]"

EXPOSE 8000

FROM base AS dev

# Install development dependencies in addition to production ones
RUN pip install --no-cache-dir ".[dev]"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM base AS prod

CMD ["uvicorn", "exam_project.asgi:application", "--host", "0.0.0.0", "--port", "8000"]