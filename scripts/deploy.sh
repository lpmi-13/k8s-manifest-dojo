if ! [ -d "/tmp/k3s-data" ]; then
  mkdir /tmp/k3s-data
fi

for i in {1..100}; do
  echo "this is log message #${i}" > /tmp/k3s-data/${i}.txt
done

# we need to set up the data and the persistent volumes first
kubectl apply -f manifests/webserver-pv.yaml

kubectl apply -f manifests/webserver-pvc.yaml

# and once the storage is set up, we can actually deploy the pods
kubectl apply -f manifests/webserver-deployment.yaml

kubectl apply -f manifests/webserver-service.yaml
