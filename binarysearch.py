"""def binarysearch(slist, value, last_index):
    length = len(slist)
    if(length==0):
        return -1
    if(length==1):
        return 0 if slist[0]==value else -1
    index = length/2
    if(slist[index]==value):
        return last_index 
    elif(value<slist[index]):
        if(length%2==0):
            last_index = last_index-length/2
        else:
            last_index = last_index-1-length/2
        return binarysearch(slist[:index], value, last_index)
    else:
        return binarysearch(slist[index:], value, last_index)"""


not_found = -1
def binarysearch(slist, value, left, right):
    while(left<=right):
        mid = (left+right)/2
        if slist[mid]==value:
            return mid
        elif value<slist[mid]:
            right = mid-1
            return binarysearch(slist, value, left, right)
        else:
            left = mid+1
            return binarysearch(slist, value, left, right)
    return -1

l = [1, 2, 3]
found = binarysearch(l, 5, 0, len(l)-1)
print found
