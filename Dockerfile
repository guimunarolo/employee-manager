FROM python:3.6

ENV TZ 'America/Sao_Paulo'

EXPOSE 8000

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
