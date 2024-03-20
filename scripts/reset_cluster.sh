# First, tear down anything currently running
./scripts/tear_down.sh

# Clear out current application manifests and copy the templates back in
rm -rf "./manifests/application/*"
cp -r "./manifests/templates" "./manifests/application"

# set up the manifests with one broken configuration
python3 ./scripts/configure.py

# And now reset the deployments with corresponding services
./scripts/deploy.sh
