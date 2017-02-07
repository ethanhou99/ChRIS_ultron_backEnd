#!/bin/bash

echo "Destroying chris containerized development environment from ./docker-compose.yml"
echo " "

echo "1-Stopping services ..."
docker-compose stop
echo " "

echo "4-Removing all containers ..."
docker-compose rm -vf 