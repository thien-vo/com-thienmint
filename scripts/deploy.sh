#!/bin/bash


echo "START PRE-DEPLOYMENT: Authentication"
echo "CURRENT PATH: `pwd`"

# [START auth]
# Decrypt the credentials we added to the repo using the key we added with the Travis command line tool
  openssl aes-256-cbc -K $encrypted_47749fd3305f_key -iv $encrypted_47749fd3305f_iv -in credentials.tar.gz.enc -out credentials.tar.gz -d

  tar -xzf authentications.tar.gz
  echo "MAKING SURE THAT THE KEYS ARE THERE"
  ls -l client-secret.json
# [END auth]

# Set the correct project to deploy to
if [ "$1" == "master" ]; then
  echo "Authenticating with master project"
  gcloud auth activate-service-account --key-file client-secret.json
  echo "Set deployment to master"
  gcloud config set project python-181206

 echo "START DEPLOYMENT: deploy.sh"
 echo "CURRENT PATH: `pwd`"

 cd app
 echo "Inside `pwd` now"
    echo "---- Installing the Python dependencies"
    pip install -r requirements.txt -t lib/
    echo "---- Deployment starts"
    gcloud app deploy app.yaml
    echo "---- Deployment ends"
 cd ..
 echo "Back in `pwd` directory now"
fi
