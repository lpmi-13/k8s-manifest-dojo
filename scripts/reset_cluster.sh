# use this for a running cluster that's been fixed, when you want to set up the next broken configuration activity

# Check if the manifests copy target directory exists, and if not, create it
if ! [ -d "./manifests/application" ]; then
  mkdir ./manifests/application
fi

# First, tear down anything currently running
./scripts/tear_down.sh

# Clear out current application manifests and copy the templates back in
rm -rf "./manifests/application/*"
cp -r "./manifests/templates/*" "./manifests/application"

# set up the manifests with one broken configuration
python3 ./scripts/configure.py

# And now reset the deployments with corresponding services
./scripts/deploy_services.sh
