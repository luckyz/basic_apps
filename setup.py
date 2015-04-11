#!/usr/bin/env python

from os import system


f = open('list.txt', 'r').readlines()
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
    elif cmd == 'apt':
        code = 'sudo apt-get install '
    elif cmd == 'remove':
        code = 'sudo apt-get remove '
    elif cmd == 'pip':
        code = 'pip install '

    #if flag == False:
    #    system('sudo -s')
    #    flag = True

    install = code + app
    system(install)
