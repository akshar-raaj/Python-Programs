#filename raising.py
class ShortWordException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast
        
try:
    text=input("Enter something\n")
    if len(text)<3:
        raise ShortWordException(len(text),3)
except EOFError:
        print "eof"
except ShortWordException as e:
        print "Length is {0}. It must be atleast {1}".format(e.length,e.atleast)
else:
    print text
        
        
        