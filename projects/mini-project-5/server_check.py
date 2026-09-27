import socket

host = "example.com"
port = 22

try:
    socket.create_connection((host, port), timeout=5)
    print(f"Status: {host} on port {port} is REACHABLE")
except Exception as e:
    print(f"Status: {host} on port {port} is NOT REACHABLE")
