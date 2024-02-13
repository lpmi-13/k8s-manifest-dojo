DATABASE_ENDPOINT=$(kubectl get svc postgres -o=jsonpath='{.spec.clusterIP}')

PGPASSWORD=supersecretproductionpassword psql -h $DATABASE_ENDPOINT -U postgres-prod -d postgres -f ./scripts/setup_users.sql