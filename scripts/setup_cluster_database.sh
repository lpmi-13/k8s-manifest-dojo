DATABASE_ENDPOINT=$(kubectl get po postgres-0 -o=jsonpath='{.status.podIP}')

PGPASSWORD=supersecretproductionpassword psql -h $DATABASE_ENDPOINT -U prod-user -f ./scripts/setup_users.sql