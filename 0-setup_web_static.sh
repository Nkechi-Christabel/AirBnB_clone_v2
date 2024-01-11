#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static.

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/
echo -e "<html>
<head>
</head>
<body>
    Hello World!
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '44i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
