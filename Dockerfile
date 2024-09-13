FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8501 8000

CMD ["sh", "-c", "uvicorn api_endpoints.routes:app --host 0.0.0.0 --port 8000 & streamlit run app/main.py"]
