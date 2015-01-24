class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.lstrip()
        ans = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        flag = True
        if str.count('+') >=2 or str.count('-') >=2 or (str.count('-') + str.count('+'))>=2:
            return 0
            
        for i in range(len(str)):
            if str[i] == '+':
                flag = True
            elif str[i] == '-':
                flag = not flag
            elif str[i] in '0123456789':
                ans = ans*10 + int(str[i])
            else:
                break
                
        if flag and ans > INT_MAX:
            ans = INT_MAX
            if not flag:
                ans = -ans
                if ans < INT_MIN:
                    ans = INT_MIN
                    

        return ans
        
if __name__ == '__main__':
    so = Solution()
    ss = "         f11484849885"
    ss1 = "+1"
    k = so.atoi(ss)
    print k, type(k)