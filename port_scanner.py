import socket   #for sockets
import sys  #for exit
from threading import Thread
import threading

print 'Socket Created'
 
host = 'agiliq.com'
ports = range(100)
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
class ConnectPortThread(Thread):
    def __init__(self, port):
        super(ConnectPortThread, self).__init__()
        self.port = port
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
            sys.exit();

    def run(self):
        try:
            self.s.connect((remote_ip , self.port))
            print 'Socket Connected to ' + host + ' on port ' + str(self.port)
        except socket.error:
            pass

def thread_count():
    return threading.active_count()

threads = []
for port in ports:
    #At some point num of thread reach a limit
    #and program gives an error
    #Make sure to never have more than 50 threads
    while True:
        if thread_count() < 50:
            break
    c = ConnectPortThread(port)
    threads.append(c)
    c.start()

[thread.join() for thread in threads]
