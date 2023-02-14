#!/usr/bin/env python3
import hashlib
from sys import argv
from socket import socket, AF_INET, SOCK_STREAM

dRcv = 1024;

stdId = 'STID_'
login = 'LGIN_'
logout = "LOUT_"
get = "GET__"
put = "PUT__"
bye = "BYE__"



# create a TCP socket
serverIP = "172.28.176.63"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect to the given Server IP, port number
clientSocket.connect((serverIP,serverPort))

# the secret student id should be taken as the command line argument
student_key = str(argv[1])

# initial handshake is to pass the student_key
# to which the server response with an ok
handshakestn = "STID_" + student_key
clientSocket.send(handshakestn);
loginResponse = clientSocket.recv(1024)

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

lginInit = "LGIN_"
for i in range(0,9999):
    pwtry = str(i).zfill(4)
    attempt = lginInit + pwtry;
    modifiedSentence = clientSocket.recv(1024).decode()
    if modifiedSentence[:3] == str(201):
        clientSocket.send('GET__')
        contentMsg = clientSocket.recv(1024);

