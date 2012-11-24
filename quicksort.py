def concatenate(left_list, pivot, right_list):
    left_list.extend(pivot)
    left_list.extend(right_list)
    return left_list

def quicksort(li):
    if len(li)==1 or len(li)==0:
        return li
    pivot = li[0]
    left_list= []
    right_list = []
    for i in range(1, len(li)):
        if(li[i]<=pivot):
            left_list.append(li[i])
        else:
            right_list.append(li[i])
    return concatenate(quicksort(left_list), [pivot], quicksort(right_list))

def qs(li):
    return quicksort(li)

import unittest
import random
class TestQuickSort(unittest.TestCase):
    def test_empty(self):
        print "Test ran"
        lst = []
        ls = qs(lst)
        self.assertEqual(len(ls), 0)

    def test_one(self):
        lst = [1]
        ls = qs(lst)
        self.assertEqual(len(ls), 1)
        self.assertEqual(ls[0], 1)

    def test_equal(self):
        lst = [1,1]
        ls = qs(lst)
        self.assertEqual(len(ls), 2)
        self.assertEqual(ls[1], 1)

    def test_random(self):
        size = random.randint(0, 10)
        lst = [random.randint(0, 100) for i in range(size)]
        ls = qs(lst)
        self.assertEqual(len(ls), size)
        lst.sort()
        self.assertEqual(ls[0], lst[0])

if __name__=="__main__":
    unittest.main()
