FROM python:3.7.3-alpine
LABEL maintainer="devcor@kevinbreit.net"

RUN apk add --no-cache mariadb-dev build-base && \
    pip install flask Flask-WTF SQLAlchemy mysqlclient bs4
COPY ssl /ssl
COPY src /src
WORKDIR /src
EXPOSE 5000/tcp
ENTRYPOINT ["python"]
CMD ["start.py"]
