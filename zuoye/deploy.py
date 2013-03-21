#!/usr/bin/python

# usage: 

# python deploy.py start/stop/status to start/stop/status nginx and uwsgi

import sys, subprocess

def syscall(command):
    return subprocess.check_output(command, shell=True)

class Status:
    nginx = 0
    uwsgi = 0

def check_status():
    """
    return Status
    Status.nginx=1
    Status.uwsgi=1
    1 means running, otherwise 0.
    """
    output = syscall("ps -ef | grep nginx && ps -ef | grep uwsgi")
    result = ""
    for line in output.splitlines():
        if 'grep nginx' in line:
            continue
        if 'grep uwsgi' in line:
            continue
        result = result + line + "\r\n"
    if 'nginx' in result:
        Status.nginx = 1
    if 'uwsgi' in result:
        Status.uwsgi = 1
    return Status

# sys.exit(int) 0 means successful termination, 2 in linux means command line syntax errors, 1 means all other kinds of errors.

if len(sys.argv) != 2:
    print 'python deploy.py start/stop/status to start/stop/status nginx and uwsgi'
    sys.exit(2)

if sys.argv[1] == 'start':
    Status = check_status()
    if Status.nginx or Status.uwsgi:
        print 'nginx or uwsgi is running, please stop them first.'
    else:
        # make sure the libs required are up to date in virtualenv: ~/devenv/lib/python2.7 and then start nginx and uwsgi.
        command = 'cd ~/ProductProject/zuoye/ZuoYeProject && ~/devenv/bin/python setup.py develop && sudo nginx && uwsgi --ini-paste-logged production.ini'
        print syscall(command)
    sys.exit(0)
elif sys.argv[1] == 'stop':
    Status = check_status()
    if Status.nginx:
        print syscall("sudo kill -QUIT `cat /usr/local/nginx/logs/nginx.pid`")
    if Status.uwsgi:
        print syscall("uwsgi --stop /var/log/pyramid/pid_5000.pid")
    print 'complete stopping nginx and uwsgi.'
    sys.exit(0)
elif sys.argv[1] == 'status':
    Status = check_status()
    if Status.nginx:
        print 'nginx is running.'
    else:
        print 'nginx is not running.'
    if Status.uwsgi:
        print 'uwsgi is running.'
    else:
        print 'uwsgi is not running.'
    sys.exit(0)
else:
    print 'python deploy.py start/stop/status to start/stop/status nginx and uwsgi'
    sys.exit(2)

