if ! [ -d "/tmp/k3s-data" ]; then
  mkdir /tmp/k3s-data
fi

python3 ./scripts/data_generator.py

# set up the namespace and the roles first
kubectl apply -f manifests/namespace.yaml

kubectl apply -f manifests/secret-read-role.yaml

kubectl apply -f manifests/webserver-serviceaccount.yaml

kubectl apply -f manifests/webserver-rolebinding.yaml

# we need to set up the data and the persistent volumes before the pods can access them
kubectl apply -f manifests/logs-processor-pv.yaml

kubectl apply -f manifests/logs-processor-pvc.yaml

# let's also set up the database (and eventually seed it with some data)
kubectl apply -f manifests/database-volumes.yaml

kubectl apply -f manifests/database-deployment.yaml

kubectl apply -f manifests/database-service.yaml

kubectl apply -f manifests/database-secrets.yaml

# and once the storage is set up, we can actually deploy the pods
kubectl apply -f manifests/webserver-deployment.yaml

kubectl apply -f manifests/webserver-service.yaml

kubectl apply -f manifests/logs-processor-deployment.yaml

kubectl apply -f manifests/logs-processor-service.yaml

kubectl apply -f manifests/user-info-deployment.yaml

kubectl apply -f manifests/user-info-service.yaml

# we probably also need some network policies and config maps
kubectl apply -f manifests/network-policy-user-info.yaml
kubectl apply -f manifests/network-policy-logs-processor.yaml
kubectl apply -f manifests/network-policy-database.yaml

kubectl apply -f manifests/config-map.yaml

# and let's also set up the data in the postgres database so the user-info
# service can query it

echo "waiting 5 seconds for database to be ready..."
sleep 5

./scripts/setup_cluster_database.sh

# and lastly, we add the monitoring stack
kubectl apply -f manifests/monitoring
