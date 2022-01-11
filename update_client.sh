#!#/bin/env bash

set -x
set -e

version=$(curl -H 'Content-type: application/json' https://git.door43.org/api/v1/version | jq -r '.version'| cut -f1 -d"+")

curl -H 'Content-type: application/json' -X POST -d "{\"options\": {\"packageName\": \"dcs_catalog_client\", \"projectName\": \"dcs-catalog-client\", \"packageVersion\": \"$version\", \"packageUrl\": \"https://github.com/unfoldingWord-dev/python-dcs-catalog-client\"}, \"swaggerUrl\": \"https://git.door43.org/swagger.catalog.json\"}" https://generator.swagger.io/api/gen/clients/python | curl $(jq -r '.link') -o client.zip

unzip client.zip

rsync -P -rvzc --delete --exclude=update_client.sh --exclude=python-client --exclude=.git* python-client/ ./

rm -rf python-client

