FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
COPY skills ./skills
COPY examples ./examples

RUN pip install --no-cache-dir .

ENTRYPOINT ["coating-mcp"]
