FROM python:3.10.4-slim-buster

ENV CELERY_BROKER_URL redis://redis:6379/0

ENV CELERY_RESULT_BACKEND redis://redis:6379/0

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]