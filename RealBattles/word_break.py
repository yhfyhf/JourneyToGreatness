import unittest

def wordBreak(s, dic):
    if len(s) == 0:
        return "" in dic
    dp = [False for _ in range(len(s)+1)]
    dp[0] = True
    for i in range(len(s)):
        if dp[i] is False:
            continue
        for w in dic:
            if w == s[i:i+len(w)]:
                dp[i+len(w)] = True
    return dp[len(s)]

# print wordBreak("dogsandcat", ["dog", "dogs", "and", "sand", "cat"])
# print wordBreak("", ["dog", "dogs", "and", "sand", "cats"])
# print wordBreak("", [])

class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(wordBreak("dogsandcat", ["dog", "dogs", "and", "sand", "cat"]))
    def test2(self):
        self.assertFalse(wordBreak("", ["dog", "dogs", "and", "sand", "cat"]))
    def test3(self):
        self.assertTrue(wordBreak("dog", ["dog", "dogs", "and", "sand", "cat"]))
            
unittest.main()
