f=open("using_file_text")
while True:
    text=f.readline()
    if(len(text)==0):
        break
    print text,
f.close()