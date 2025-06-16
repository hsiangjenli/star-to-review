#!/bin/bash
set -e

echo "Building images..."
docker-compose build

echo "Starting FL server and 3 clients..."
docker-compose up -d

echo "All containers are up."
echo "To add a new client dynamically, run:"
echo "  docker run --rm -d --network code_56-daily-review-adapflower_flower_fl_net -e SERVER_ADDRESS=fl-server:8080 -e CLIENT_ID=clientX flower-client"
