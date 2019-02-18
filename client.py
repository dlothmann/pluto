import socket
import time

#CONFIG

#IP
IP = '192.168.0.136'
#Port
PORT = 22




ctimes = 5
i = 0
connect = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

e = None
try:
    s.connect((IP, PORT))

    while i < ctimes:
        if s.send("test".encode()):
            connect = "yay"

        else:
            connect = "doof"
    i += 1
except socket.error as e:
    if e != None:
        connect = "FAIL"



#time.sleep(10)
s.close()

print(connect)
