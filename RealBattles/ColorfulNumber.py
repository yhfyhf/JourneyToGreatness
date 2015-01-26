
def isColorful(num):
    num = list(str(num))
    num = map(int, num)
    numset = set()
    for i in xrange(1, len(num)):
        for j in xrange(len(num)):
            if i + j >= len(num):
                continue
            #print num[j:j+i+1]
            if product(num[j: j+i+1]) in numset:
                return False
            else:
                numset.add(product(num[j:j+i+1]))
    return True

                

def product(lt):
    return reduce(lambda x,y: x*y, lt)

if __name__ == '__main__':
    num = 3245
    print isColorful(num)