FROM python:3.10-slim

WORKDIR /random-app

COPY ./requirements.txt /random-app/requirements.txt
COPY app/ /random-app

RUN pip install --no-cache-dir --upgrade -r /random-app/requirements.txt

RUN rm -f /random-app/requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
