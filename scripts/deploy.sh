if ! [ -d "/tmp/k3s-data" ]; then
  mkdir /tmp/k3s-data
fi

for i in {1..100}; do
  echo "this is log message #${i}" > /tmp/k3s-data/${i}.txt
done

# we need to set up the data and the persistent volumes first
kubectl apply -f manifests/webserver-pv.yaml

kubectl apply -f manifests/webserver-pvc.yaml

# let's also set up the database (and eventually seed it with some data)
kubectl apply -f manifests/database-volumes.yaml

kubectl apply -f manifests/database-deployment.yaml

kubectl apply -f manifests/database-service.yaml

# and once the storage is set up, we can actually deploy the pods
kubectl apply -f manifests/webserver-deployment.yaml

kubectl apply -f manifests/webserver-service.yaml

kubectl apply -f manifests/backend-deployment.yaml

kubectl apply -f manifests/backend-service.yaml

# we probably also need some network policies and config maps
kubectl apply -f manifests/network-policy.yaml

kubectl apply -f manifests/config-map.yaml
