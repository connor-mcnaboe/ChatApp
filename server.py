# Created: 03/18/19
# Author: Connor McNaboe
# Purpose: Establishes server-side connection 

import socket
import sys

def server_connection():
    HOST = None               # Symbolic name meaning all available interfaces
    PORT = 50007              # Arbitrary non-privileged port
    s = None
    conn = None 
    # Check information for given hostname, port, IP protocol (IvP4,6), TCP (SOCK_STREM)

    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)  
        except OSError as msg:
            print('could not open socket' + str(msg))
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except OSError as msg:
            print('could not open socket' + str(msg))
            s.close()
            s = None
            continue
        break
    if s is None:
        sys.exit(1)
    
    while conn == None: 
        print("Waiting for connection...")
        conn, addr = s.accept()
    return conn, addr

# Setup port and wait for client connection
conn, addr = server_connection()

with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)  # Recives data from client program, with a maximum of 1024 bytes 
        print(data)
        if not data: break      # Breaks of nothing is recived 
        conn.send(data)         # Sends data back to client 

