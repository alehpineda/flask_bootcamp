FROM python:3.7.5-buster

LABEL maintainer="Alex Pineda <alehpineda@gmail.com>"

COPY ./ ./app

WORKDIR ./app

RUN pip3 install -r requirements.txt

ENV FLASK_ENV=development
ENV FLASK_APP=app.py

EXPOSE 5000 80

RUN chmod u+x ./entrypoint.sh
RUN chmod u+x ./wait_for_it.sh

ENTRYPOINT ["./wait_for_it.sh", "db:5432", "--", "./entrypoint.sh"]
