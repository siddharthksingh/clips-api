FROM python:3.13

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

CMD ["bash", "-c", "python app/seed.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]