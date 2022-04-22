# https://fastapi.tiangolo.com/deployment/
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR /app

# Copying this separately prevents re-running pip install on every code change.
COPY requirements.txt /app

# Install dependencies.
RUN pip install -r requirements.txt

# Copy local code to the container image.
COPY . /app

CMD gunicorn app.main:app --bind :$PORT --worker-class="uvicorn.workers.UvicornWorker" --timeout=0