def isAdditive(num):
    return testOneDigit(num) or testTwoDigits(num)

def testOneDigit(num):
    if num < 100:
        return False
    num = map(int, list(str(num)))
    for i in xrange(2, len(num)):
        if num[i] != num[i-1] + num[i-2]:
            return False
    return True

def testTwoDigits(num):
    if num < 100000:
        return False
    # convert 1234 => [1,2,3,4]
    num = map(int, list(str(num)))

    for i in xrange(5, len(num), 2):
        if num[i-1]*10+num[i] != num[i-3]*10+num[i-2] + num[i-5]*10+num[i-4]:
            return False
    return True

if __name__ == '__main__':
    
    # True
    print isAdditive(112)
    print isAdditive(11235)
    print isAdditive(12122436)
    # False
    print isAdditive(111)
    print isAdditive(12345)


                    