DATABASE_ENDPOINT=$(kubectl get svc postgres -o=jsonpath='{.spec.clusterIP}')

PGPASSWORD=supersecretproductionpassword psql -h $DATABASE_ENDPOINT -U prod-user -f ./scripts/setup_users.sql