for resource in deploy svc sts secrets configmap roles rolebinding sa networkpolicy pvc pv; do
  kubectl delete $resource -n dojo --all;
done

# also tear down the monitoring stack
for resource in svc deploy sa clusterrole clusterrolebinding; do
  kubectl delete $resource -n kube-system kube-state-metrics
done