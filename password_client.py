import socket

# Connect to server
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect("/tmp/ipc_password.sock")

# Request a 12-character password
sock.send("12".encode())

# Receive and print password
password = sock.recv(1024).decode()
print(f"Edge-generated password: {password}")
sock.close()