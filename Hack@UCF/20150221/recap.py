import socket, time

#get location of remote computer and service
ip = "104.131.81.195"
port = 4444

#make socket
s = socket.socket()

#use socket to make connection
s.connect((ip,port))


print s.recv(20)
s.send("126\n")

time.sleep(1)

print s.recv(20)
s.send("256\n")

time.sleep(1)

print s.recv(20)
s.send("0\n")

time.sleep(1)

print s.recv(20)
s.send("0\n")

time.sleep(1)

print s.recv(20)
input()
    
