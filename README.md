# K3s Surprise (working title)

This is a k3s cluster with configuration to present several common scenarios to debug:

- DNS issues
- Liveness/Readiness probe issues
- ResourceLimit issues

The actual problem will be chosen on startup of the applications, and you'll see there's an issue by querying pod status or looking in logs.

We may get to the point where there's an actual application that you can see misbehaving, but in this PoC, I think we'll assume there's no production traffic and all the issues will present themselves in the absence of actual load on the system.

## Architecture

Because k3s runs with containerd, we can't just run locally built images, so we need to set up a locally running container registry.

Besides that, we'll have a few containers running in the cluster

- a flask webserver
- ...
- ...

## Running locally (the whole point)

First, you'll need to have k3s installed and running. The easiest way to do that is to follow the [quickstart guide](https://docs.k3s.io/quick-start).

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
