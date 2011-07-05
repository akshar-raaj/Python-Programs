"""f=open("diff_operation_file_text","w")
#text=f.read()
text=""
if(len(text)==0):
    print "No text"
else:
    print text
f.write("Writing in w mode\n")
f=open("diff_operation_file_text","r")
text=f.read()
print text
f.close()"""
"""import pickle
f=open("diff_operation_file_object","w")
li=[1,2,3]
pickle.dump(li,f)
f.close()"""
import pickle
import os
f=open("diff_operation_file_object","r")
isEmpty=os.path.getsize("diff_operation_file_object")==0
"""li2=[3,4,5]
pickle.dump(li2,f)
f.close()"""
if not isEmpty:
    text=pickle.load(f)
    print text
else:
    f=open("diff_operation_file_object","w")
    li=[1,2,3]
    pickle.dump(li,f)
f.close()


