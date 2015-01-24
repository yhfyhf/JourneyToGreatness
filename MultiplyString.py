# TODO Use enumerate to optimize the readbility
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        res = [0]* (len(num1)+len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                res[i+j] += int(num1[i])*int(num2[j])
                
        for k in xrange(len(res[:-1])): # impossible to carry at highest
            if res[k] >= 10:
                res[k+1] += res[k]/10
                res[k] = res[k]%10

        res = map(str, res)
        while len(res) > 1 and res[-1] == '0':
            res.pop()
        
        return ''.join(res[::-1])

num1 = '340143712837123782323'
num2 = '100000000000083834783478472843'

so = Solution()
print so.multiply(num1, num2)
    
                
                
                

            
                        
        