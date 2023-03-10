FROM python:alpine

WORKDIR /stocks_products

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python3 manage.py runserver 0.0.0.0:8000