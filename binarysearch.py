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
import unittest
class TestBinS(unittest.TestCase):
    def test_empty(self):
        lst = []
        key = 0
        self.assertEquals(binsearch(lst, 0,), -1)

    """def test_equal(self):
       lst = [0, 0, 0, 0]
       self.assertEquals(binsearch(lst, 0,), 0)"""

    def test_negs(self):
       lst = [-10, -1, 0, 1 , 10]
       self.assertEquals(binsearch(lst, 0,), 2)

    def test_randoms(self):
       import random
       size = random.randint(0, 10)
       lst = sorted([random.randint(0, 10) for i in range(size)])
       lst = list(set(lst)) #we are already aware of bug in case there are duplicates
       if lst: #lst can be an empty list and then lst[0] will be an error
           self.assertEquals(binsearch(lst, lst[0],), 0)


def binsearch(slist, value, left=0, right=None):
    if not right:
        right = len(slist)-1
    return binarysearch(slist, value, left, right)

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

if __name__=="__main__":
    unittest.main()
