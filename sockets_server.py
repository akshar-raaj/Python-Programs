import socket
import sys
import threading
from Queue import Queue

messages = Queue()

class BroadCastThread(threading.Thread):

    def run(self):
        global messages
        while True:
            message, conn_addr = messages.get()
            for thread in threading.enumerate():
                if isinstance(thread, ChatThread):
                    if not conn_addr==thread.conn_addr:
                        thread.conn.sendall(message)


class ChatThread(threading.Thread):
    def __init__(self, conn, addr):
        super(ChatThread, self).__init__()
        self.conn = conn
        self.addr = addr
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        self.conn_addr = addr[0] + ':' + str(addr[1])

    def run(self):
        while True:
            global messages
            data = self.conn.recv(1024)
            if data=="\r\n":
                break
            messages.put((data, self.conn_addr))
        self.conn.close()
        print "Conection closed with " + self.addr[0] + ":" + str(self.addr[1])

HOST = ''
PORT = 8888

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print "Can't create socket"
    sys.exit()
print "socket created"

try:
    sock.bind((HOST, PORT))
except socket.error:
    print "Cant bind"
    sys.exit()
print 'Socket bind complete'

sock.listen(10)
print 'Socket now listening'

BroadCastThread().start()
while True:
    conn, addr = sock.accept()
    ChatThread(conn, addr).start()
