# -*- coding: utf-8 -*-

# http://www.themianjing.com/uber-%E7%94%B5%E9%9D%A2/

import Queue

def online_people(log):
    # @param log: a list of tuples ("user a", 5, 10)
    # @return res: a list of tuples of # of online people in each timestamp
    pq = Queue.PriorityQueue()
    cnt, res = 0, []
    for e in log:
        pq.put((e[1], 1))
        pq.put((e[2], -1))
        
    while not pq.empty():
        t = pq.get()
        cnt += t[1]
        if len(res) >= 1 and t[0] == res[-1][0]:
            res[-1][1] = cnt
        else:
            res.append([t[0], cnt])
    return res

if __name__ == '__main__':
    log = [("a", 5, 10), ("b", 6, 8), ("c", 10, 11)]
    res = online_people(log)
    print res
