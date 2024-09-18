FROM python:3.12-slim

WORKDIR /app

COPY server.py /app/

EXPOSE 80


CMD [ "python", "server.py" ]
