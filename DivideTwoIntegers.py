class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        flag = +1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            if abs(dividend) < abs(divisor):
                return 0
                flag = -1
                
        res = 0
        a, b = abs(dividend), abs(divisor)
        while a >= b:
            sum, cnt = b, 1
            while sum + sum < a:
                sum += sum
                cnt += cnt
            a -= sum
            res += cnt
        if flag == -1:
            return -res
        return res

    # binary operator
    def divide2(self, dividend, divisor):
        flag = +1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            if abs(dividend) < abs(divisor):
                return 0
        flag = -1
                    
        res = 0
        a, b = abs(dividend), abs(divisor)
        while a >= b:
            sum, cnt = b, 1
            while sum<<1 < a:
                sum <<= 1
                cnt <<= 1
            a -= sum
            res += cnt
        if flag == -1:
            return -res
        return res

if __name__ == '__main__':
    so = Solution()
    print so.divide2(43421,3244)