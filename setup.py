#!/usr/bin/python

from os import system


f = open('requirements.txt', 'r').readlines()
for line in f:
    flag = False
    command = line.split('|')
    cmd = command[0]
    app = command[1]

    if cmd == 'ppa':
        code = 'sudo add-apt-repository '
    elif cmd == 'update':
        code = 'sudo apt-get update '
    elif cmd == 'upgrade':
        code = 'sudo apt-get upgrade'
    elif cmd == 'pipu':
        code = 'sudo pip install -U '
    elif cmd == 'apt':
        code = 'sudo apt-get install '
    elif cmd == 'remove':
        code = 'sudo apt-get remove '
    elif cmd == 'pip':
        code = 'sudo pip install '

    #if flag == False:
    #    system('sudo -s')
    #    flag = True

    install = 'yes | ' + code + app
    system(install)
