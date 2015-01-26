# 11222101 => 12101
# reduce duplicated ones

def compress(num):
    # convert 123 to [1,2,3]
    num = map(int, list(str(num)))
    flag = num[0]
    res = [num[0]]
    for i in xrange(1, len(num)):
        if num[i] == flag:
            continue
        else:
            res.append(num[i])
            flag = num[i]

    # convert [1,2,3] to 123
    res = ''.join(map(str, res))
    return int(res)

if __name__ == '__main__':
    print compress(11222335444401)