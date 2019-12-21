import socket

#open a file
passwdfile = open("wordlist.txt", "r")
outfile = open("newlist.txt", "w")

arr=[]
while True:
    tmp = passwdfile.readline()
    if not tmp: break
    arr.append(tmp)
passwdfile.close()

for l in arr:
    outfile.write(l)
outfile.close()
