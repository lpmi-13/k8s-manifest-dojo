docker build -t flask-webserver -f webserver/Dockerfile webserver/
docker tag flask-webserver localhost:5001/flask-webserver
docker push localhost:5001/flask-webserver

docker build -t logs-processor -f logs-processor/Dockerfile logs-processor/
docker tag logs-processor localhost:5001/logs-processor
docker push localhost:5001/logs-processor
