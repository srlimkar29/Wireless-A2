import socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect("/tmp/ipc_socket.sock")
data = ",".join(str(x) for x in range(1, 51))  # Sends numbers 1-50
sock.send(data.encode())
print(sock.recv(1024).decode())  # Prints stats from server
sock.close()