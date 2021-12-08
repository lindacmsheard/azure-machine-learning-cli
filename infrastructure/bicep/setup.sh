#!/bin/bash

source .env

az deployment sub create \
  --name bootcampBicepDeployment \
  --location $LOCATION \
  --template-file main.bicep \
  --parameters project=$PROJECT rgLocation=$LOCATION