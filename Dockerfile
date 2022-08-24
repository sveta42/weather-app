FROM python:3.8-alpine
RUN pip install --upgrade pip
EXPOSE 5000
WORKDIR /app
COPY ./. .
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
