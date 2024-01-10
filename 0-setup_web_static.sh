#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static.

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/
echo "<html><head><title>Test Page</title></head><body>Test content</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/; }" /etc/nginx/sites-available/default
sudo service nginx restart
