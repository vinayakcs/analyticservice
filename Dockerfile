FROM python:3.5

ADD . .
RUN pip install -r req
EXPOSE 5000