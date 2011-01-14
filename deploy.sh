#!/bin/sh

# deploy steps here: copy env-conf/* to nginx and uwsgi
# deploy html/py codes to nginx/html

git pull
sudo kill -QUIT `cat /usr/local/nginx/logs/nginx.pid`
sudo rm /usr/local/nginx/html/recordsound.net -rf
sudo cp recordsound.net /usr/local/nginx/html/ -r
sudo rm /usr/local/nginx/html/realspymonitor.net -rf
sudo cp realspymonitor.net /usr/local/nginx/html/ -r
sudo cp env-conf/nginx.conf /usr/local/nginx/conf/
sudo nginx
