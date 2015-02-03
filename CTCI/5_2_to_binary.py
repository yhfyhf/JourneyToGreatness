"""
given a real number between 0 and 1, print the binary representation.
If the number cannot be represent in 32 chars, print error
"""

def ToBinary(num):
    # @param num: a number
    if num < 0 or num > 1:
        return "number range error"
    res = []
    for _ in xrange(32):
        num *= 2
        if num >= 1:
            res.append('1')
            num -= 1
        elif num > 0:
            res.append('0')
        else:
            break
    if num:
        return "ERROR"
    return '0.' + ''.join(res)

if __name__ == '__main__':
    print ToBinary(0.25)
    print ToBinary(0.8125)
    print ToBinary(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000049034)
        