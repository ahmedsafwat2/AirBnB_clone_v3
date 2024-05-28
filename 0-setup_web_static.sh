#!/usr/bin/env bash
#  sets up your web servers for the deployment of web_static

apt-get update -y
apt-get upgrad -y
apt-get install nginx -y
ufw allow 'Nginx HTTP'

mkdir -p /data/ /data/web_static/ /data/web_static/releases/
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

data="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$data" | tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data/

conf="server {
        listen 80 default_server;
        index index.html index.htm;
        server_name mahmoudelwazeer.tech;
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;

        location /hbnb_static/{
                alias /data/web_static/current/;
        }

}"

echo "$conf" | tee /etc/nginx/conf.d/hbnb.conf
service nginx restart
