FROM python:3.7-alpine

WORKDIR /app
COPY web-app/ .

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt

ENV FLASK_APP app.py

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]
