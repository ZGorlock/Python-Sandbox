import socket

#get location of remote computer and service
ip = "54.201.246.241"
port = 1338

#make socket
s = socket.socket()

#use socket to make connection
s.connect((ip,port))

s.settimeout(2)

try:
    print s.recv(1)
except socket.timeout:
    pass

s.send("Testing\n")

info = s.recv(1)
print info

input()
