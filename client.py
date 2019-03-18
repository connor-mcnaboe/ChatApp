import socket
import sys

def client_connection(): 
	HOST = '192.168.0.110'    # The remote host, hardcoded connection
	PORT = 50007              # The same port as used by the server
	s = None
	for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
		af, socktype, proto, canonname, sa = res
		try:
			s = socket.socket(af, socktype, proto)
		except OSError as msg:
			s = None
			continue
		try:
			s.connect(sa)
		except OSError as msg:
			s.close()
			s = None
			continue
		break
	
	if s is None:
		print('could not open socket')
		sys.exit(1)
	return s

s = client_connection()
with s:
    while True:
        cont = input('Cont?')
        if cont == 'Y': 
            s.sendall(b'Stop')
            data = s.recv(1024)
            print(data)
            break
        else: 
            s.sendall(b'Recived data')
            data = s.recv(1024)
            print(data)