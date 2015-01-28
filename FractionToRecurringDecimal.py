class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        positive = True
        if numerator/denominator < 0:
            positive = False
            numerator = abs(numerator)
            denominator = abs(denominator)
        circleset = {}
        dec_part = []
        position = 0
        int_part = str(numerator/denominator)
        numerator = numerator % denominator
        while numerator % denominator:
            cur_digit = numerator*10/denominator
            if numerator not in circleset:
                dec_part.append(str(cur_digit))
                circleset[numerator] = position
                position += 1
                numerator = numerator*10 % denominator
            else:
                div = circleset[numerator]
                dec_part = dec_part[:div] + ['('] + dec_part[div:] + [')']
                break
        dec_part = ''.join(dec_part)
        if not positive:
            int_part = "-" + int_part
        if not dec_part:
            return int_part
        return int_part + "." + dec_part

if __name__ == '__main__':
    so = Solution()
    # 1 99
    # 1 333
    # -50 8
    # 1, 214748364 0.00(00000046...)
    
    print so.fractionToDecimal(1000,5)
    print so.fractionToDecimal(1,333)
    print so.fractionToDecimal(1,99)
    print so.fractionToDecimal(22,7)
    print so.fractionToDecimal(-50,8)
    print so.fractionToDecimal(1,214748364)


