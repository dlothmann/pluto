import socket
import sys
import threading
import queue
#CONFIG

#IP
IP = '192.168.0.136'
#Port
startPort = 0
endPort = 65534
maxPort = 65535

#diff = endPort - startPort

q = queue.Queue

def check(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((IP, p))
    if result == 0:
        print ("Port {} || Open".format(p))
    else:
        print ("Port {} || Close".format(p))


#threads = diff/4

threads = []
try:
    if endPort < maxPort  and startPort >= 0:

            
        for port in range(startPort,endPort+1):

            process = threading.Thread(target=check,name=port,args=[port])
            process.start()
            threads.append(process)
            
            #process.join()
        for process in threads:
            process.join()
                
    else:
        print("Kein gültiger Port")
        s.close()

    
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#s.close()