# Check if the manifests copy target directory exists, and if not, create it
if ! [ -d "./manifests/application" ]; then
  mkdir ./manifests/application
done

# First, tear down anything currently running
./scripts/tear_down.sh

# Then, we set up the registry, since we'll need to push container images to that so our cluster can run them
./scripts/start_registry.sh

# Next, we'll build all the images
./scripts/build_containers.sh

# And now we can deploy those containers as deployments with corresponding services
./scripts/deploy.sh
