FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir scikit-learn joblib

ENV APP=app.py

CMD ["python", "app.py"]
