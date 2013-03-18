import unittest

def check_anagrams(str1, str2):
    #Complexity of this algorithm seems O(NlogN)
    l1 = []
    l2 = []
    #O(N)
    for each in str1:
        l1.append(each)
    #O(N)
    for each in str2:
        l2.append(each)
    #O(NlogN)
    return sorted(l1) == sorted(l2)

def check_anagrams_2(str1, str2):
    d1 = {}
    d2 = {}
    are_anagrams = True
    for each in str1:
        d1[each] = 1 if each not in d1 else d1[each]+1
    for each in str2:
        d2[each] = 1 if each not in d2 else d2[each]+1
    for k1, v1 in d1.iteritems():
        if k1 not in d2.keys():
            are_anagrams = False
            break
        v2 = d2.pop(k1)
        if not v1==v2:
            are_anagrams = False
            break
    if d2:
        are_anagrams = False
    return are_anagrams
        

class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(check_anagrams("debit card", "bad credit"))
        self.assertTrue(check_anagrams_2("debit card", "bad credit"))

    def test_nonagrams(self):
        self.assertFalse(check_anagrams("hello", "world"))
        self.assertFalse(check_anagrams_2("hello", "world"))

    def test_with_empty_strings(self):
        self.assertTrue(check_anagrams("", ""))
        self.assertTrue(check_anagrams_2("", ""))

    def test_with_one_empty_string(self):
        self.assertFalse(check_anagrams("", "nonempty"))
        self.assertFalse(check_anagrams_2("", "nonempty"))

        self.assertFalse(check_anagrams("nonempty", ""))
        self.assertFalse(check_anagrams_2("nonempty", ""))

    def test_with_spaces(self):
        self.assertFalse(check_anagrams("", " "))
        self.assertFalse(check_anagrams_2("", " "))

if __name__ == "__main__":
    unittest.main()
