docker stop postgres

docker rm postgres

# we are intentionally using port 6432 on the host so you don't forget, like I did, to shut down the local
# docker postgres database and try to connect to the one in the k3s cluster. Because this one is bound to
# all interfaces (0.0.0.0), that's what will get picked up even if you try to use the clusterIP, and it will
# fail
docker run -d -p 6432:5432 -e POSTGRES_PASSWORD=password --restart always --name postgres postgres:latest

echo "waiting 5 seconds for the database to be ready..."
sleep 5

PGPASSWORD=password psql -h localhost -U postgres -f ./scripts/setup_users.sql