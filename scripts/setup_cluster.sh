# First, we set up the registry, since we'll need to push container images to that so our cluster can run them
./scripts/start_registry.sh

# Next, we'll build all the images
./scripts/build_containers.sh

# And now we can deploy those containers as deployments with corresponding services
./scripts/deploy.sh
