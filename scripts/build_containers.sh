docker build -t flask-webserver -f webserver/Dockerfile webserver/
docker tag flask-webserver localhost:5001/flask-webserver
docker push localhost:5001/flask-webserver
