#!/usr/bin/python

# usage: 

# python deploy.py start/stop/status to start/stop/status nginx and uwsgi

import sys, subprocess

def syscall(command):
    return subprocess.check_output(command, shell=True)

def check_status():
    """
    return 1 if is running, otherwise 0.
    """
    output = syscall("ps -ef | grep nginx && ps -ef | grep uwsgi")
    result = ""
    for line in output.splitlines():
        if 'grep nginx' in line:
            continue
        if 'grep uwsgi' in line:
            continue
        result = result + line + "\r\n"
    if len(result) == 0:
        print "nginx and uwsgi is not running."
        return 0
    else:
        if 'nginx' in result:
            print 'nginx is running.'
        if 'uwsgi' in result:
            print 'uwsgi is running.'
        return 1

if len(sys.argv) != 2:
    print 'python deploy.py start/stop/status to start/stop/status nginx and uwsgi'
    sys.exit(2) # 2 in linux means command line syntax errors, 1 means all other kinds of errors.

if sys.argv[1] == 'start':
    # make sure the libs required is up to date in virtualenv: ~/devenv/lib/python2.7
    command = 'cd ~/ProductProject/zuoye/ZuoYeProject && ~/devenv/bin/python setup.py develop && sudo nginx && uwsgi --ini-paste-logged production.ini'
    print syscall(command)
    sys.exit(0) # 0 means successful termination.
elif sys.argv[1] == 'stop':
    if check_status():
        print syscall("sudo kill -QUIT `cat /usr/local/nginx/logs/nginx.pid` && uwsgi --stop /var/log/pyramid/pid_5000.pid")
        print 'complete stopping nginx and uwsgi.'
    sys.exit(0)
elif sys.argv[1] == 'status':
    check_status()
    sys.exit(0)
else:
    print 'python deploy.py start/stop/status to start/stop/status nginx and uwsgi'
    sys.exit(2)

