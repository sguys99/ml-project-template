# FROM python:3.12-slim

# # Install uv.
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# # Copy the application into the container.
# COPY . /app

# # Install the application dependencies.
# WORKDIR /app
# RUN uv sync --frozen --no-cache

# EXPOSE 8080
# EXPOSE 8081

# # Run the application.
# CMD ["uv", "run", "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8080"]
