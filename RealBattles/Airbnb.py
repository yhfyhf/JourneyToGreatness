import unittest

def checkIntersect(r1, r2):
    # return True or False
    x1, X1, y1 ,Y1 = r1
    x2, X2, y2, Y2 = r2
    if x2 > X1 or y2 > Y1 or X2 < x1 or Y2 < y1:
        return False
    return True
    

def countIntersect(lt):
    pass


"""
#1. make_trie
#2. 

"""

END = '$'
def make_trie(words):
    root = {}
    for word in words:
        r = root
        for c in word:
            if c not in r:
                r[c] = {}
            r = r[c]
        r[END] = {}
    return root

def search(dic, m):
    t = make_trie(dic)
    res = []
    def dfs(i, j, tree, buff):
        if END in tree:
            res.append(buff)
        if m[i][j] not in tree:
            return 
        # m[i][j] in tree
        next_tree = tree[m[i][j]]
        next_buff = buff+m[i][j]
        # up
        if i - 1 >= 0:            
            dfs(i-1, j, next_tree, next_buff)
            # up left
            if j - 1 >= 0:
                dfs(i-1, j-1, next_tree, next_buff)
        # down
        if i + 1 < len(m):
            dfs(i+1, j, next_tree, next_buff)
            # down right
            if j + 1 < len(m[0]):
                dfs(i+1, j+1, next_tree, next_buff)
        # left
        if j - 1 >= 0:
            dfs(i, j-1, next_tree, next_buff)
            # left down
            if i + 1 < len(m):
                dfs(i+1, j-1, next_tree, next_buff)
        # right
        if j + 1 < len(m[0]):
            dfs(i, j+1, next_tree, next_buff)
            # right up
            if i - 1 >= 0: 
                dfs(i-1, j+1, next_tree, next_buff)
                
        ''' Eight direction   
        for k in range(max(0, i-1), min(len(m), i+2)):
            for l in range(max(0, j-1), min(len(m[0]), j+2)):
                if k != i and l != j:
                    dfs(k, l, next_tree, next_buff)
        '''
    for i in range(len(m)):
        for j in range(len(m[0])):
            dfs(i, j, t, '')
    return set(res)
            
        
        


class Test(unittest.TestCase):
    """
    def t1(self):
        # x1 x2 y1 y2
        lt = [(1,3,1,3), (2,3,2,4), (4,5,3,4), (4,6,2,4)]
        self.assertEqual(countIntersect(lt), 4)
    """
    def t2(self):
        matrix = [
            ['a', 'b', 'c', 'd'],
            ['x', 'e', 't', 'c'],
            ['w', 'a', 'v', 'c'],
            ['z', 'b', 'i', 'o'],
        ]
        dic = ['ab', 'a', 'bc', 'abc', 'aba', 'aictexa', 'zci']
        self.assertEqual(search(dic, matrix), set(['ab', 'a', 'bc', 'abc', 'aba', 'aictexa']))


"""
toJSON, not interview question
"""
def toJSON_JayXon(dic):
    res = "{"
    for k,v in dic.iteritems():
        if type(v) is dict:
            v = toJSON(v)
        res += str(k)+':'+str(v) + ","
    if res[-1] == ",":
        res = res[:-1]
    return res + "}"


def toJSON(dic):
    res = "{"
    for k in dic:
        if type(dic[k]) is not dict:
            res += str(k)+':'+str(dic[k]) + ","
        else:
            res += str(k) + ':' + toJSON(dic[k]) + ","
    if res[-1] == ",":
        res = res[:-1]
    return res + "}"


def test_toJSON():
    dic = {}
    dic['a'] = 'b'
    dic['b'] = {'a': 'c'}
    print toJSON(dic)



def max_reservation(lt):
    # like house robber problem
    if len(lt) < 2:
        return 0 if len(lt) == 0 else lt[0]
    # dp = [0 for x in range(len(lt))]
    res = 0
    past, yest = lt[0], max(lt[0], lt[1])
    for i in range(2, len(lt)):
        today = max(past + lt[i], yest)
        res = max(today, res)
        past = yest
        yest = today
    return res



print max_reservation([4,9,6])
print max_reservation([4,10,3,1,5])

# if __name__ == '__main__':
#     unittest.main()
