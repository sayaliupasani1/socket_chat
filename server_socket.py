import socket
import sys
import time

host = ''
#ip = socket.gethostbyname(host)
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#try:
s.bind((host, port))
#except:
#    print 'Bind failed'

print 'Socket binding complete'

s.listen(15)
print 'Socket is now listening for incoming connections'
#time.sleep(10)
#s.close()
#print 'Closing socket connection now'
con,addr = s.accept()
while 1:
    print 'I am called'
    #con,addr = s.accept()
    print con
    print addr
    print 'Connected with' + str(addr)

    data= con.recv(1024)
    print data
    #con.sendall(data)
    if not data:
        break;
    con.sendall(data)
    
s.close()
con.close()
print 'Socket closed'
