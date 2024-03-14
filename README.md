# K3s Dojo

This is a k3s cluster with configuration to present several common scenarios to debug:

- DNS issues
- Liveness/Readiness probe issues
- ResourceLimit issues
- RBAC access to secrets issues

The actual problem will be chosen on startup of the applications, and you'll see there's an issue by querying pod status or looking in logs.

We may get to the point where there's an actual application that you can see misbehaving, but in this PoC, I think we'll assume there's no production traffic and all the issues will present themselves in the absence of actual load on the system.

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

Once that's all set up, you can run the `setup_cluster.sh` script to get the base configuration running.

```sh
./scripts/setup_cluster.sh
```

> run this from the root directory of the project

## Entering the Dojo

The cluster will be started with one problem chosen at random, and you'll need to figure out what it is and how to fix it.

> The first place to look is in the spec for the misbehaving service. Since the problem is a misconfigured manifest, that's where you need to fix things. Use the errors to figure out which spec to look in.

Potential issues:

- misconfigured deployment
- misconfigured ports
- misconfigured service accounts
- misconfigured namespaces
- misconfigured volume constraints
- misconfigured resource requests and/or limits
- misconfigured database access

> Most of these will probably cause issues with the pods starting up, so it should be fairly obvious that something's wrong, but I'm going to try and have a bunch of variations to keep it spicy

You should be able to visit the grafana dashboard to see if something's up. You can see what IP to use to access the dashboard via:

```sh
kubectl -n monitoring get svc
```

You'll see something like this:

```sh
NAME                 TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
prometheus-service   NodePort   10.43.1.191    <none>        8080:30000/TCP   6m47s
grafana              NodePort   10.43.213.62   <none>        3000:32000/TCP   6m47s
```

And so you can access `http://10.43.213.62:3000` in the browser to go to the dashboard. The default admin username and password, respectively, are "admin" and "admin".

...you can also just see what pods are running via:

```sh
kubectl -n dojo get po
```

## Resetting the cluster

If, for any reason, you want to reset everything, you can run the k3s "kill all" script at `/usr/local/bin/k3s-killall.sh` (the k3s installer should put it into the `$PATH`). After that, to bring the cluster back up, you can run `sudo systemctl restart k3s`.