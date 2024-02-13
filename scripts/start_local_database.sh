docker stop postgres

docker rm postgres

docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=password --restart always --name postgres postgres:latest

echo "waiting 5 seconds for the database to be ready..."
sleep 5

PGPASSWORD=password psql -h localhost -U postgres -f ./scripts/setup_users.sql