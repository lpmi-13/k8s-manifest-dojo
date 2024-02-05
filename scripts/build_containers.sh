docker build -t flask-webserver -f webserver/Dockerfile webserver/
docker tag flask-webserver localhost:5001/flask-webserver
docker push localhost:5001/flask-webserver

docker build -t flask-backend -f backend/Dockerfile backend/
docker tag flask-backend localhost:5001/flask-backend
docker push localhost:5001/flask-backend
