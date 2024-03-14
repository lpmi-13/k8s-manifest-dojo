DATABASE_ENDPOINT=$(kubectl -n dojo get po postgres-0 -o=jsonpath='{.status.podIP}')

docker run \
  -it \
  --network host \
  -e PGPASSWORD=supersecretproductionpassword \
  -v ./scripts:/var/scripts \
  postgres:16 \
  /bin/sh -c \
  "psql -h $DATABASE_ENDPOINT -U prod-user -f /var/scripts/setup_users.sql"