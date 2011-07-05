import time
try:
    f=open("using_file_text","r")
    while True:
        text=f.readline()
        """if len(text)==0:
            break"""
        print text,
        time.sleep(1)
except EOFError:
    print "eof"
except KeyboardInterrupt:
    print "interrupt"
finally:
    f.close()
