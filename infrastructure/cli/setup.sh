#!/bin/bash

# load environment variables from a .env file
source .env

echo $RG

R=$((RANDOM%1000))
RG="${RG}_${R}"

echo $RG

echo "Working in subscription:"
echo "-- $(az account show -o tsv --query name) --"
echo "Continue? (y/N)"  
read  

if [ $REPLY = 'y' ]; then

    echo "Creating resource group ..."

    az group create -n $RG --location $LOCATION
    echo "$RG created."
    echo "RG=$RG" >> ../../.env

    echo "Setting defaults..."

    az config set defaults.group=$RG
    az config set defaults.location=$LOCATION

    az config get defaults
else
    echo "exiting."
fi