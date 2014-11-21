class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def add(self, num1, num2):
        # 21, 111
        n1, n2 = num1[::-1], num2[::-1]
        res, carry = "", 0
        for i in range(min(len(n1), len(n2))):
            tmp = int(n1[i]) + int(n2[i])
            res += str(tmp%10 + carry)
            carry = 0
            if tmp >= 10:
                carry = 1

        if len(n1)>len(n2):
            for i in range(len(n2), len(n1)):
                tmp = int(n1[i]) + carry
                res += str(tmp%10)
                carry = 1 if tmp/10 else 0
        if len(n2)>len(n1):
            for i in range(len(n1), len(n2)):
                tmp = int(n2[i]) + carry
                res += str(tmp%10)
                carry = 1 if tmp/10 else 0
        if carry:
            res += str(carry)
        return res[::-1]

from random import randint
so = Solution()
for i in range(1000):
    a = randint(1000000000000000000000000000000000, 1000000000000000000000000000000000)
    b = randint(1000000000000000000000000000000000, 1000000000000000000000000000000000)
    assert so.add(str(a),str(b)) == str(a+b)


            
                        
        