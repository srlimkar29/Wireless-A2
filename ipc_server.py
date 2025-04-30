import socket, statistics
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind("/tmp/ipc_socket.sock")
sock.listen(1)
conn, _ = sock.accept()
data = conn.recv(1024).decode()
numbers = list(map(float, data.split(',')))
mean = statistics.mean(numbers)
median = statistics.median(numbers)
stdev = statistics.stdev(numbers) if len(numbers) > 1 else 0
conn.send(f"Mean: {mean}, Median: {median}, StdDev: {stdev}".encode())
conn.close()