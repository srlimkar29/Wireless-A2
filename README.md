COMP40660: Advances Wireless Networks | Assignment 2: Edge Computing

Group Members: Shubham Limkar (24202802), Rishabh Lingsugur (24212867)

===================================

Part 1: Docker Virtualization  
- Docker Hub Image:
  https://hub.docker.com/r/shubhamlimkar/avengers-image

Part 2: Docker Networking & Offloading
- Password Generator Code:
  Server: password_server.py
  Client: password_client.py

GitHub Repo Like for all files:
https://github.com/srlimkar29/Wireless-A2/tree/MK1

===================================

Part 1 Steps:
# Pull and run images
docker run hello-world
docker run busybox echo "Hello from BusyBox"
docker run -d -p 8080:80 nginx

# Show running containers
docker ps -a

# Verify images
docker images

# Stop and remove all containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

echo "<h1>Group Members : Shubham & Rishabh</h1>" > index.html

docker run -d -p 8090:80 -v "D:\UCD\Spring Semester\COMP40660 Advances Wireless Networking\A2\index.html:/usr/share/nginx/html/index.html" nginx

# Start Ubuntu container
docker run -it ubuntu /bin/bash

# Inside images
apt update && apt install nano iputils-ping

# List files
ll

# Create directory
mkdir /Avengers

echo "Group Members : Shubham & Rishabh" > /Avengers/members.txt

cd Avengers

cat members.txt

exit

# List all the images to get container id
docker ps -a

# Commit
docker commit <container_id> shubhamlimkar/avengers-image

docker push shubhamlimkar/avengers-image

# Confirm the same
docker images

===================================

Part 2 Steps:

# Create a Bridge Network
docker network create alpine-net

# Run 3 Alpine Containers
# Attach them to the network and assign custom names (alpine1, alpine2, alpine3)
docker run -dit --name alpine1 --network alpine-net alpine sh
docker run -dit --name alpine2 --network alpine-net alpine sh
docker run -dit --name alpine3 --network alpine-net alpine sh

# Test Connectivity
docker exec -it alpine1 sh
ping alpine2
ping alpine3
exit

# Create a Shared Volume for IPC
docker volume create ipc-vol

# Build Custom Images for IPC
docker build -t ipc-server -f Dockerfile.server .
docker build -t ipc-client -f Dockerfile.client .

# Run server (share volume for IPC socket)
docker run -d --name server -v ipc-vol:/tmp ipc-server

# Run client (same volume)
docker run --name client -v ipc-vol:/tmp ipc-client

===================================
