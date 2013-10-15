import socket
import sys
import threading

class ChatThread(threading.Thread):
    def __init__(self, conn, addr):
        super(ChatThread, self).__init__()
        self.conn = conn
        self.addr = addr
        print 'Connected with ' + addr[0] + ':' + str(addr[1])

    def run(self):
        while True:
            data = self.conn.recv(1024)
            print "data " + data + str(len(data))
            if data=="\r\n":
                break
            self.conn.sendall(data)
        self.conn.close()
        print "Conection closed with " + addr[0] + ":" + str(addr[1])

HOST = ''
PORT = 8888

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print "Can't create socket"
    sys.exit()

print "socket created"

try:
    s.bind((HOST, PORT))
except socket.error:
    print "Cant bind"
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

while 1:
    conn, addr = s.accept()
    t = ChatThread(conn, addr)
    t.start()

s.close()
