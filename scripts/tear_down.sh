for resource in deploy svc pv pvc sts secrets configmap roles rolebinding sa networkpolicy; do
  kubectl delete $resource -n dojo --all;
done