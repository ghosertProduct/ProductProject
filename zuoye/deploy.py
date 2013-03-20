#!/usr/bin/python

# usage: 

# python deploy.py start/stop to start/stop nginx and uwsgi

import sys, subprocess

if len(sys.argv) != 2:
    print 'python deploy.py start/stop to start/stop nginx and uwsgi'
    sys.exit(2)
if sys.argv[1] == 'start':
    subprocess.call("sudo nginx && uwsgi --ini-paste-logged ./ZuoYeProject/production.ini", shell=True)
elif sys.argv[1] == 'stop':
    subprocess.call("sudo kill -QUIT `cat /usr/local/nginx/logs/nginx.pid` && uwsgi --stop /var/log/pyramid/pid_5000.pid", shell=True)
else:
    print 'python deploy.py start/stop to start/stop nginx and uwsgi'
    sys.exit(2)

