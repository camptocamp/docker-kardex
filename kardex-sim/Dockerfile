from alpine:3.11

RUN apk upgrade musl && apk add --no-cache python3

COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]
