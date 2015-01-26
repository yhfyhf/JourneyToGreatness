def maxSubArray(lt):
    max_so_far, max_ending_here = 0, 0
    for i in xrange(len(lt)):
        max_ending_here = max_ending_here + lt[i]
        # like DP, if < 0, not possible
        if max_ending_here < 0:
            max_ending_here = 0
        # max_so_far extend only when get larger
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


if __name__ == '__main__':
    lt =[-2, -3, 100, 1, -10, -10]
    print maxSubArray(lt)