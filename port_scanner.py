# adapted from the youtube video "Python3 For Pentesting - Developing A Port Scanner" 
# link - "https://www.youtube.com/watch?v=d3D8PAZV51g"

#! usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

# hackthissite.org ip: "137.74.187.104"
# ports: 443 (https), 21 (ftp), 22 (ssh)

host = input("Enter the IP you want to scan: ")
port = int(input("Enter the Port you want to scan: "))

def port_scanner(port):
    if s.connect_ex((host, port)):
        print("The Port is Closed")
    else:
        print("The Port is Open")

port_scanner(port)
