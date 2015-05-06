import unittest

def checkIntersect(r1, r2):
    # return True or False
    x1, X1, y1 ,Y1 = r1
    x2, X2, y2, Y2 = r2
    if x2 > X1 or y2 > Y1 or X2 < x1 or Y2 < y1:
        return False
    return True
    

def countIntersect(lt):
    # O(N^2)
    r_set = set()
    for r1 in range(len(lt)):
        for r2 in range(r1+1, len(lt)):
            if checkIntersect(lt[r1], lt[r2]):
                if lt[r1] not in r_set:
                    r_set.add(lt[r1])
                if lt[r2] not in r_set:
                    r_set.add(lt[r2])

    return len(r_set)

#lt = [(1,3,1,2), (2,5,1,4), (1,3,5,6), (4,6,3,6), (1, 3, 5, 6), (2.5, 5.5, 5.5, 3.5)]
#lt2 = [(1,2,1,2)]
#print countIntersect(lt2)

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


def search0(dic, m):
    # TODO mark visited
    if len(m) < 1:
        return
    t = make_trie(dic)
    res = set()
    def dfs(i, j, tree, buff):
        if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]):
            return
        if END in tree:
            if buff not in res:
                res.add(buff)
        if m[i][j] not in tree:
            return
        child = tree[m[i][j]]
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x != 0 or y != 0:
                    dfs(i+x, j+y, child, buff + m[i][j])
                    
    for i in range(len(m)):
        for j in range(len(m[0])):
            dfs(i, j, t, '')
    dfs(0, 0, t, '')
    return res

def test_search0():
    m = [
        list("aakm"),
        list("qisb"),
        list("rdrn"),
        list("belb")
    ]

    dic = ["aaa", "air", "airbed", "aaa", "nbl", "mai"]
    print search0(dic, m)
    
test_search0()

    
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



#print max_reservation([4,9,6])
#print max_reservation([4,10,3,1,5])

# if __name__ == '__main__':
#     unittest.main()
