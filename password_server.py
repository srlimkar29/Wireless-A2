import socket
import secrets

# Set up IPC socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind("/tmp/ipc_password.sock")
sock.listen(1)

print("Password server ready...")
conn, _ = sock.accept()

# Receive password length from client
length = int(conn.recv(1024).decode())

# Generate secure password (URL-safe, no confusing symbols)
password = secrets.token_urlsafe(length)

# Send back to client
conn.send(password.encode())
conn.close()