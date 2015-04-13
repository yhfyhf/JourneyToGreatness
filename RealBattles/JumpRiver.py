# -*- coding: utf-8 -*-
"""
给一个0/1数组R代表一条河，0代表水，1代表石头。起始位置R[0]等于1，
初速度为1. 每一步可以选择以当前速度移动，或者当前速度加1再移动。只能停留在石头上。问最少几步可以跳完整条河流。

给定数组为R=[1,1,1,0,1,1,0,0]，最少3步能过河：
第一步先提速到2，再跳到R[2]；
第二步先提速到3，再跳到R[5]；
第三步保持速度3，跳出数组范围，成功过河。
"""

def jump1(R):
    # @param R: stones and waters
    cache = {}
    def dfs(idx, speed):
        if idx >= len(R):
            return 0
        if (idx, speed) in cache:
            return cache[(idx, speed)]
        
        ret = -1
        if R[idx]:
            # two possible dfs
            ret0 = dfs(idx + speed, speed)
            ret1 = dfs(idx + speed + 1, speed + 1)

            if ret0 >= 0 and ret1 >= 0:
                ret = min(ret0, ret1) + 1
            elif ret0 < 0 and ret1 < 0:
                ret = -1
            else:
                ret = max(ret0, ret1) + 1
        cache[(idx, speed)] = ret
        return ret
    return dfs(0, 1)

if __name__ == '__main__':
    R = [1,1,1,0,1,1,0,0]
    print jump1(R)
