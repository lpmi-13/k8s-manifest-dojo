docker build -t flask-webserver -f service-src/webserver/Dockerfile service-src/webserver/
docker tag flask-webserver localhost:5001/flask-webserver
docker push localhost:5001/flask-webserver

docker build -t logs-processor -f service-src/logs-processor/Dockerfile service-src/logs-processor/
docker tag logs-processor localhost:5001/logs-processor
docker push localhost:5001/logs-processor

docker build -t user-info -f service-src/user-info/Dockerfile service-src/user-info/
docker tag user-info localhost:5001/user-info
docker push localhost:5001/user-info

docker build -t load-generator -f service-src/load-generator/Dockerfile service-src/load-generator/
docker tag load-generator localhost:5001/load-generator
docker push localhost:5001/load-generator