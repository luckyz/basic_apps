#!/usr/bin/python

from os import system


f = open('requirements.txt', 'r').readlines()
for line in f:
    flag = False
    command = line.split('|')
    cmd = command[0]
    app = command[1]

    if cmd == 'ppa':
        prefix = 'yes ENTER | '
        code = 'sudo add-apt-repository '
    elif cmd == 'update':
        prefix = ''
        code = 'sudo apt-get update'
    elif cmd == 'upgrade':
        prefix = ''
        code = 'sudo apt-get upgrade'
    elif cmd == 'pipu':
        prefix = ''
        code = 'sudo pip install -U '
    elif cmd == 'apt':
        prefix = 'yes | '
        code = 'sudo apt-get install '
    elif cmd == 'remove':
        prefix = 'yes | '
        code = 'sudo apt-get remove '
    elif cmd == 'pip':
        prefix = 'yes | '
        code = 'sudo pip install '

    install = prefix + code + app
    system(install)
