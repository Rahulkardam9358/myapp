FROM python:3.10-slim-buster
WORKDIR myapp
COPY . .
RUN pip install -r requirements.txt