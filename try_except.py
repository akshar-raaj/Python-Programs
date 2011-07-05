text=""
try:
    text=input("Enter something")
except EOFError:
    print "Eof"
except KeyboardInterrupt:
    print "Keyboard interrupt"
else:
    print text