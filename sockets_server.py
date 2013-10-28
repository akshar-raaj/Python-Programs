import socket
import sys
import threading

messages = []
condition = threading.Condition()

class BroadCastThread(threading.Thread):

    def run(self):
        global messages
        while True:
            condition.acquire()
            if not messages:
                condition.wait()
            message, conn_addr = messages.pop(0)
            condition.release()
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
            condition.acquire()
            messages.append((data, self.conn_addr))
            condition.notify()
            condition.release()
        self.conn.close()
        print "Conection closed with " + self.addr[0] + ":" + str(self.addr[1])

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

BroadCastThread().start()
while 1:
    conn, addr = s.accept()
    t = ChatThread(conn, addr)
    t.start()

s.close()
