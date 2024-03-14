# you probably don't need to care about this unless you're changing something about the user-info service
docker stop postgres

docker rm postgres

# we are intentionally using port 6432 on the host so you don't forget, like I did, to shut down the local
# docker postgres database and try to connect to the one in the k3s cluster. Because this one is bound to
# all interfaces (0.0.0.0), that's what will get picked up even if you try to use the clusterIP, and it will
# fail
docker run -d -p 6432:5432 -e POSTGRES_PASSWORD=password --restart always --name postgres postgres:16

echo "waiting 5 seconds for the database to be ready..."
sleep 5

docker run -it --network host -e PGPASSWORD=password -v ./scripts:/var/scripts postgres:16 /bin/sh -c "psql -h localhost -p 6432 -U postgres -f /var/scripts/setup_users.sql"