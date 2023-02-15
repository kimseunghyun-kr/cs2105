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

FDATA = "100_" 
HAND = "200_" 
LOGIN = "201_"
LGOUT = "202_"
HMATCH = "203_"
INVSTID = "401_"
INVOP = "402_" 
INVPW = "403_"
INVHSH= "404_"
PERMDEN = "405_"
INVREQ = "406_"
HEADRCV = 4

pwLeft = 8
serverIP = "172.28.176.63"
serverPort = 4444
clientSocket = socket(AF_INET, SOCK_STREAM)

def fileGet:
    clientSocket.send(get)
    getResponse = clientSocket.recv(HEADRCV).decode()
    if getResponse == FDATA:
        contentLen = "";
        curr = "";
        while(curr != "_") :
            contentLen += curr;
            curr = clientSocket.recv(1).decode()
        contentLen = int(contentLen)
        
        data = clientSocket.recv(contentLen).decode()
        return data
    else:
        print("unable to find hash with resp code %d".format(getResponse))
    

def pwCrack(pwLeft):
    i = 0
    while(i < 10000):
        if(pwLeft == 0):
            break;
        pwtry = str(i).zfill(4)
        attempt = login + str(4) + pwtry;
        loginResponse = clientSocket.recv(HEADRCV).decode()
        if loginResponse == LOGIN:
            data = fileGet()
            md5HashandPut(data)
            pwLeft-=1;
    
    if(pwLeft > 0):
        print("could not find all pw")
        return -1

    return 0;
        


def md5HashandPut(data){
    hashedresult = hashlib.md5(data);
    sendput = put + str(32) + hashedresult
    clientSocket.send(sendput);
    response = clientSocket.recv(HEADRCV)
    if response == INVHSH:
        print("wrong hash")
    else if response == HMATCH:
        print('correct hash')
    else:
        print('unknown error with response code %d'.format(response))
    
}            

# create a TCP socket
# connect to the given Server IP, port number
clientSocket.connect((serverIP,serverPort))

# the secret student id should be taken as the command line argument
student_key = str(argv[1])

# initial handshake is to pass the student_key
# to which the server response with an ok
handshakestn = stdId + str(len(student_key)) student_key
clientSocket.send(handshakestn);
handshakeResp = clientSocket.recv(HEADRCV)

# if server responds with OK code proceed with the hack

data = ""
if handshakeResp == HAND:

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
    pwCrack(pwLeft)
    clientSocket.send(logout);
    logoutResp = clientSocket.recv(HEADRCV);
    
    if logoutResp == LGOUT:
        print("logout");
    else:
        print("unknown error with response code %d".format(logoutResp))
    

