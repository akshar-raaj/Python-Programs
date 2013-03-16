import unittest

def check_anagrams(str1, str2):
    l1 = []
    l2 = []
    for each in str1:
        l1.append(each)
    for each in str2:
        l2.append(each)
    return sorted(l1) == sorted(l2)

class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(check_anagrams("debit card", "bad credit"))

    def test_nonagrams(self):
        self.assertFalse(check_anagrams("hello", "world"))

if __name__ == "__main__":
    unittest.main()
