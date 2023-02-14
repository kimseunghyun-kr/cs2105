#!/usr/bin/env python3
import hashlib
from sys import argv
from socket import socket, AF_INET, SOCK_STREAM

# create a TCP socket

# connect to the given Server IP, port number

# the secret student id should be taken as the command line argument
student_key = str(argv[1])

# initial handshake is to pass the student_key
# to which the server response with an ok

# if server responds with OK code proceed with the hack

# try out all possible passwords
# for each password
#        check the server response code for each password to see if the login was successful
#        if successful login
#            send request for data
#            receive the data (this is binary data hence you do not have to use "decode")
#            compute the digest
#            send the digest back to server
#            receive response from server
#            send logout request
#            receive response from server
