def binarysearch(slist, value):
    length = len(slist)
    if(length==0):
        return -1
    if(length==1):
        return 0 if slist[0]==value else -1
    index = length/2
    if(slist[index]==value):
        return 1
    elif(value<slist[index]):
        return binarysearch(slist[:index], value)
    else:
        return binarysearch(slist[index:], value)

l = [1, 2, 3, 4, 5]
found = binarysearch(l, 0)
if found>=0:
    print "Element found"
else:
    print "Element not found"
