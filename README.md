## Microservice boilerplate, FastAPI + MongoDB + nginx (for HTTPS)

Quite simple example with FastAPI behind nginx, talking to MongoDB.
Nothing special, but a good starting point though.

### How to generate self-signed SSL cert for nginx:

```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout cert.key -out cert.crt
```

Now just move `cert.key` and `cert.crt` to folder `conf/nginx/ssl` and you're all set!

### How to run:

Just `docker-compose up` and it will fire up in few minutes, as the building process will be finished.
