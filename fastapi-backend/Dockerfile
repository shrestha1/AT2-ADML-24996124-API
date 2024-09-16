FROM python:3.11.4-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgomp1 \
    # Other dependencies
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "routes:app", "--host", "0.0.0.0", "--port", "8000"]