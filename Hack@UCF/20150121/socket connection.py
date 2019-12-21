import socket

#get location of remote computer and service
ip = "54.201.246.241"
port = 1337

#make socket
s = socket.socket()

#use socket to make connection
s.connect((ip,port))

print s.recv(20)
input()
