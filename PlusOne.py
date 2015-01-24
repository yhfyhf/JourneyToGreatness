class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits = digits[::-1]
        digits[0] += 1
        carry = 0
        for i in xrange(len(digits)):
            digits[i] += carry
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                carry = 1
            else:
                carry = 0
                break
        if carry:
            digits.append(1)
        return digits[::-1]

    # not reverse, 6 times faster
    def plusOne2(self, digits):
        carry = 0
        for i in xrange(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                carry = 1
            else:
                carry = 0
                break
        if carry:
            digits.insert(0, 1)
        return digits
                    
            