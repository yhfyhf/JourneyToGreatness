class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        def getVersion(version):
            res = []
            tmp = 0
            for i in version:
                if i == '.':
                    res.append(tmp)
                    tmp = 0
                else:
                    tmp += tmp*10 + int(i)
            res.append(tmp)
            res.reverse()
            return res
        v1, v2 = getVersion(version1), getVersion(version2)
        #print v1, v2
        while v1 and v2:
            t1, t2= v1.pop(), v2.pop()
            if t1 > t2:
                return 1
            if t1 < t2:
                return -1
        while v1:
            if v1.pop() == 0:
                continue
            else:
                return 1
        while v2:
            if v2.pop() == 0:
                continue
            else:
                return -1
        return 0

if __name__ == '__main__':
    so = Solution()
    print so.compareVersion("1.1", "1.1.0")
    
                    
                
