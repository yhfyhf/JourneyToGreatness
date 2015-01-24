def insertsort(l):
    if len(l) <= 1:
        return l
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
    return l

if __name__ == '__main__':
    l = [2,4,7,0,6,10,1]
    print insertsort(l)