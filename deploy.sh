#!/bin/sh

# deploy steps here: copy env-conf/* to nginx and uwsgi
# deploy html/py codes to nginx/html

sudo kill -QUIT `cat /usr/local/nginx/logs/nginx.pid`
sudo rm /usr/local/nginx/html/realrecorder.net -rf
sudo cp realrecorder.net /usr/local/nginx/html/ -r
sudo cp env-conf/nginx.conf /usr/local/nginx/conf/
sudo nginx
