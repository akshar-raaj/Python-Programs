import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Failed to create socket"
    sys.exit()

print "Socket created"

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print "Could not resolve"
    sys.exit()

print "IP address is " + remote_ip

s.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ipaddress ' + remote_ip

message = "GET / HTTP/1.1\r\n\r\n"

try:
    s.sendall(message)
except socket.error:
    print "Send failed"
    sys.exit()

print 'Message send successfully'

reply = s.recv(4096)

print reply

s.close()
