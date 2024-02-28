for resource in deploy svc sts secrets configmap roles rolebinding sa networkpolicy pvc pv; do
  kubectl delete $resource -n dojo --all;
done
