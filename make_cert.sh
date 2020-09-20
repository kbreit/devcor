#!/bin/bash

mkdir -p ssl
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
    -subj "/C=US/ST=Illinois/L=Chicago/O=Globomantics/CN=crm.kevinbreit.net" \
    -keyout ssl/key.pem -out ssl/cert.pem

