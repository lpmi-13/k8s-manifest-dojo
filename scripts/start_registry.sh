docker stop private-registry

docker rm private-registry

# we're binding this to port 5001 just in case we want something else to be able to use the standard 5000 port
docker run -d -p 5001:5000 --restart always --name private-registry registry:latest
