#
#Python 3 File
#

import socket
import sys
import threading
import argparse

#
#Author is Dominik Lothmann
#https://github.com/dlothmann
#Project Pluto
#




# Command Line Options definition
parser = argparse.ArgumentParser(description='Arguments for this programm.')
parser.add_argument('-H','--Host', metavar='', required=True, help='Host Adress you would scan')
parser.add_argument('-p1','--port1',type=int, metavar='', required=True, help='From Port. When only this is given you scan only this port.')
parser.add_argument('-p2','--port2',type=int, metavar='',help='To Port')
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', '--all', action='store_true', help='Shows closed AND open Ports.')

args = parser.parse_args()

#Take Command Line Options to Variables
arg1 = args.Host
arg2 = args.port1
arg3 = args.port2
url = arg1

#Set Port1 to Port2 when only the Start Port is given.
if arg3 is None:
    arg3 = arg2

#Exit when my second Port is greater than my first port
if arg3 < arg2:
    print("Wrong Input. Please Check with -h")
    sys.exit()

#Create the Hostname from URL or Host (arg1)
IP = socket.gethostbyname(url)

#Set the Start Port of the Scan, the end port of the scan and the max port number
startPort = arg2
endPort = arg3
maxPort = 65535

threads = []
oPorts = []
cPorts = []

#Check is port open or not and save the open or closed port in array oPorts or cPorts
def check(item):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((IP, item))
    if result == 0:
        oPorts.append(item)
    else:
        cPorts.append(item)

#Print all Open Ports
def printOpen():
        print("Open Ports")
        if len(oPorts) != 0:
            print("|",end="")
        else:
            print("---",end="")
        for i in oPorts:
            print("{}|".format(i),end="")
        print()

#Print all Closed Ports
def printClosed():
        print("Closed Ports")
        if len(cPorts) != 0:
            print("|",end="")
        else:
            print("---",end="")
        for i in cPorts:
            print("{}|".format(i),end="")


try:
#check if ports are ok for scanning
    if endPort < maxPort  and startPort >= 0:
#create for every portcheck a thread
        for port in range(startPort,endPort+1):

            process = threading.Thread(target=check,name=port,args=[port])
            process.start()
            threads.append(process)
#close every thread after finishing the check
        for process in threads:
            process.join()
#Print the result of the check
        if args.all:
            printOpen()
            printClosed()
        elif len(oPorts) != 0:
            printOpen()
        else:
            print("No host online or no open port in this port Range")
            sys.exit()


               
    else:
        print("Port not in Range 0 - 65535")
        s.close()
        sys.exit()

    
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()
