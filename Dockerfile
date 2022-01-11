FROM python:3.9

ENV HOME /root
WORKDIR /root

COPY . .

RUN pip3 install -r requirements.txt

#ENV FLASK_APP='App:logistics'
ENV FLASK_ENV=production
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0
ENV DEBUG=0

EXPOSE 5000

ENTRYPOINT FLASK_APP=App:logistics flask run --h 0.0.0.0
