FROM python:3.11.8-slim-bullseye AS builder
WORKDIR /code
COPY requirements.txt app.py /code/
RUN pip install /code/requirements.txt
CMD ["python3", "app.py"]


