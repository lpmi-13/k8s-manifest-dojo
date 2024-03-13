if ! [ -d "/tmp/k3s-data" ]; then
  mkdir /tmp/k3s-data
fi

python3 ./scripts/data_generator.py

# set up the namespace and the roles first
kubectl apply -f manifests/application/namespace.yaml

kubectl apply -f manifests/application/secret-read-role.yaml

kubectl apply -f manifests/application/webserver-serviceaccount.yaml

kubectl apply -f manifests/application/webserver-rolebinding.yaml

# we need to set up the data and the persistent volumes before the pods can access them
kubectl apply -f manifests/application/logs-processor-pv.yaml

kubectl apply -f manifests/application/logs-processor-pvc.yaml

# let's also set up the database (and eventually seed it with some data)
kubectl apply -f manifests/application/database-volumes.yaml

kubectl apply -f manifests/application/database-deployment.yaml

kubectl apply -f manifests/application/database-service.yaml

kubectl apply -f manifests/application/database-secrets.yaml

# and once the storage is set up, we can actually deploy the pods
kubectl apply -f manifests/application/webserver-deployment.yaml

kubectl apply -f manifests/application/webserver-service.yaml

kubectl apply -f manifests/application/logs-processor-deployment.yaml

kubectl apply -f manifests/application/logs-processor-service.yaml

kubectl apply -f manifests/application/user-info-deployment.yaml

kubectl apply -f manifests/application/user-info-service.yaml

# we probably also need some network policies and config maps
kubectl apply -f manifests/application/network-policy-user-info.yaml
kubectl apply -f manifests/application/network-policy-logs-processor.yaml
kubectl apply -f manifests/application/network-policy-database.yaml

kubectl apply -f manifests/application/config-map.yaml

# and let's also set up the data in the postgres database so the user-info
# service can query it

echo "waiting 5 seconds for database to be ready..."
sleep 5

./scripts/setup_cluster_database.sh

# and now we add the kube-state-metrics stack
kubectl apply -f manifests/kube-state-metrics

# followed by prometheus and grafana
kubectl apply -f manifests/prometheus
kubectl apply -f manifests/grafana

# and lastly, let's add some background load to the cluster
kubectl apply -f manifests/load-generator
