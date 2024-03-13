for resource in deploy svc sts secrets configmap roles rolebinding sa networkpolicy pvc pv; do
  kubectl delete $resource -n dojo --all;
done

# also tear down the monitoring stack
for resource in svc deploy sa clusterrole clusterrolebinding; do
  kubectl delete $resource -n kube-system kube-state-metrics;
done

# get rid of all the resources related to prometheus and grafana
for resource in configmap deploy svc; do
  kubectl delete $resource -n monitoring --all;
done

# remove the load-generator pods
kubectl delete deploy -n load --all