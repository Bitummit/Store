FROM python:3.9.12-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /store

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY Store Store
COPY manage.py manage.py
COPY backend backend

#
#EXPOSE 8000
#
#CMD python manage.py runserver 0.0.0.0:8000