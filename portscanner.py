#import socket module to handle network connections
import socket

def scan_port(ip, port):
    #create a socket object and attempt to connect to the specified port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #set a 1 second timeout for the connection attempt
    s.settimeout(1)
    try:
        #connect to the specified IP and port
        s.connect((ip, port))
        #if the connection is successful, print that the port is open
        print(f"[+] Port {port} is open")
    #if the connection fails, it will raise an exception
    except:
        pass
    #close the socket
    s.close()

#ask the user for the target IP address
target_ip = input("Enter target IP: ")

#scan ports from 1 to 1024
for port in range(1, 1025):
    #scan each port on the target IP
    scan_port(target_ip, port)
