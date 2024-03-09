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

## Running locally (the whole point)

First, you'll need to have k3s installed and running. The easiest way to do that is to follow the [quickstart guide](https://docs.k3s.io/quick-start).

You'll also need `python` and the `psql` command line utility installed.

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

> It's also possible that we'll have a script to randomly trigger an issue, but I haven't worked out how to do that yet, since depending on the resource affected, we might need to manually delete it and recreate it.

Potential issues:

- misconfigured deployment
- misconfigured ports
- misconfigured service accounts
- misconfigured namespaces
- misconfigured volume constraints
- misconfigured resource requests and/or limits
- misconfigured database access

> Most of these will probably cause issues with the pods starting up, so it should be fairly obvious that something's wrong, but I'm going to try and have a bunch of variations to keep it spicy

In theory, there will be a web front end that you can access locally to confirm everything is fine, but that's still to come.

## Resetting the cluster

If, for any reason, you want to reset everything, you can run the k3s "kill all" script at `/usr/local/bin/k3s-killall.sh` (the k3s installer should put it into the `$PATH`). After that, to bring the cluster back up, you can run `sudo systemctl restart k3s`.