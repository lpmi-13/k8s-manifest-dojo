# K8s Dojo

Learning to read and configure kubernetes manifests is an important foundational skill, and so this project will help you get some practice with that. I wanted more practice myself, so I built this to give myself a place to troubleshoot potential typos in the yaml.

You'll be presented with a k3s cluster with configuration to present several common scenarios to debug:

- misconfigured deployment
- misconfigured ports
- misconfigured service accounts
- misconfigured namespaces
- misconfigured volume constraints
- misconfigured resource requests and/or limits
- misconfigured database access
- misconfigured health checks
- misconfigured network policies

The actual problem will be chosen on startup of the applications, and you'll see there's an issue by querying pod status or looking in container logs. There's also a grafana pod with a few dashboards based on prometheus data that might also be helpful.

> NOTE: All of the issues will be with the yaml manifests in the `manifests/application` directory. You won't need to change any application code to fix them.

## Architecture

Because k3s runs with containerd, we can't just run locally built images, so we need to set up a locally running container registry.

Besides that, we'll have a few containers running in the cluster

- a flask webserver
- a server to deal with logs-processing (a bit contrived, but useful for local volume mounts)
- a server to interact with a database table about users
- a load generator making requests to the flask webserver that trigger downstream queries to the other services

## Running locally (the whole point)

First, you'll need to have k3s installed and running. The easiest way to do that is to follow the [quickstart guide](https://docs.k3s.io/quick-start).

You'll also need `python3` and the `docker` cli installed.

If, while following the above instructions (it's basically just a script to run), you encounter this error:

```
error: error loading config file "/etc/rancher/k3s/k3s.yaml": open /etc/rancher/k3s/k3s.yaml: permission denied
```

Follow the steps [here](https://devops.stackexchange.com/a/16044).

Once that's all set up, you can run the `full_setup_cluster.sh` script to get the base configuration running.

```sh
./scripts/full_setup_cluster.sh
```

> run this from the root directory of the project

## Entering the Dojo

The cluster will be started with one problem chosen at random, and you'll need to figure out what it is and how to fix it. Depending on what the issue is, it might take up to 30 seconds for it to be apparent.

> The first place to look is in the spec for the misbehaving service. Since the problem is a misconfigured manifest, that's where you need to fix things. Use the errors to figure out which manifest to look in. You can also check the grafana dashboards for clues.

Potential issues:

- misconfigured deployment
- misconfigured ports
- misconfigured service accounts
- misconfigured namespaces
- misconfigured volume constraints
- misconfigured resource requests and/or limits
- misconfigured database access
- misconfigured health checks
- misconfigured network policies

> Most of these will probably cause issues with the pods starting up, so it should be fairly obvious that something's wrong, but I'm going to try and have a bunch of variations to keep it spicy

You should be able to visit the grafana dashboard to see if something's up. You can see what local IP to use to access the dashboard via:

```sh
kubectl -n monitoring get svc
```

You'll see something like this:

```sh
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
prometheus-service   ClusterIP   10.43.174.175   <none>        8080/TCP   14m
grafana              ClusterIP   10.43.120.225   <none>        3000/TCP   14m
node-exporter        ClusterIP   10.43.136.80    <none>        9100/TCP   14m
```

And so you can access `http://10.43.120.225:3000` in the browser to go to the dashboard. The default admin username and password, respectively, are "admin" and "admin".

...you can also just see what pods are running via:

```sh
kubectl -n dojo get po
```

Once you've identified the issue and fixed it, you can set up the next issue by running the `scripts/next_exercise.sh` script. That will pick another misconfiguration at random and redeploy all the services. Follow the same steps from above to troubleshoot and fix it.

## Resetting the cluster from scratch

If, for any reason, you want to reset everything, you can run the k3s "kill all" script at `/usr/local/bin/k3s-killall.sh` (the k3s installer should put it into the `$PATH`). After that, to bring the cluster back up, you can run `sudo systemctl restart k3s`.