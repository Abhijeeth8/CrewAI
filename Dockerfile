FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv streamlit

# Copy pyproject + lock file first
COPY pyproject.toml uv.lock ./

# Sync dependencies
RUN uv sync

# Copy the rest of the app
COPY . .

# Set src/ as importable module root
ENV PYTHONPATH="/app/src"

EXPOSE 8501

# Start the app
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
