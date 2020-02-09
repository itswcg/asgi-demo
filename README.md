## asgi-demo
Some examples of asgi application.
* HTTP
* HTTP/2
* Websocket

## Usage
```bash
# sync
# python manage.py runserver 

# async
# http
daphne -b 0.0.0.0 -p 8000 asgi.asgi:application 
or
uvicorn asgi.asgi:application 
# http/2
daphne -e ssl:8000:privateKey=localhost+1-key.pem:certKey=localhost+1.pem asgi.asgi:application
# websocket

```