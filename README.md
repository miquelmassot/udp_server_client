# UDP Server and Client

This is an example of a UDP server and client written in Python. The server and client can be run on the same machine or on different machines.

## Usage

The server will broadcast a message to all clients that connect to it.

### Server

The server can be run with the following command:

```bash
python server.py
```

The server will broadcast on UDP port 50000.

### Client

The client can be run with the following command:

```bash
python client.py
```

The client will connect to the all UDP broadcasts port 50000.
