FROM python:3.10-slim

# Install basic tools
RUN apt-get update && apt-get install -y git curl

# Set workdir
WORKDIR /app

# Install litellm with proxy extras
RUN pip install "litellm[proxy]"

# Copy config file if needed
COPY config.yaml .

# Default command
CMD ["litellm", "--config", "config.yaml"]
