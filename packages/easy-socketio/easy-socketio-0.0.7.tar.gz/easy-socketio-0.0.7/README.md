## Easy SocketIO

Easy SocketIO is a wrapper build around [python-socketio](https://github.com/miguelgrinberg/python-socketio) that handles a simple queue and threading.

```
pip install easy-socketio
```

Example with default configs:

```python
from easy_socketio import socketio

socketio.start_server()

# Wait for connections....

# Send message to all clients

socketio.send("Hello clients")

```

Example with more detailed configurations:

```python
from easy_socketio import socketio

# Threaded flag starts the server in a background thread, default is True

socketio.start_server(
    host="127.0.0.1", 
    port=5000, 
    threaded=True, 
    cors=True, 
    static_files={'/': {'content_type': 'text/html'}}
)

# Wait for connections....

# Send message to a specific client

socketio.send(msg="Hello client", event="message", to="client_sid_here")
```