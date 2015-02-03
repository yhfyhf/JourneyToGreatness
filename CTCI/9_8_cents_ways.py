# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
# TODO
def make_change_2d(n, coins=[1, 5, 10, 25]):
    m = len(coins)
    dp = [[0 for x in xrange(m)] for y in xrange(n+1)]
    for i in xrange(m):
        dp[0][i] = 1

    for i in xrange(1, n+1):
        for j in xrange(m):
            # inlcude s[j]
            x = dp[i-coins[j]][j] if i-coins[j] >= 0 else 0
            # exclude [j]
            y = dp[i][j-1] if j >= 1 else 0
            # sum up
            dp[i][j] = x + y
    return dp[n][m-1]
                

def make_change(n, coins=[1, 5, 10, 25]):
    # dp[i] stores the number of solution for value i
    # use n+1 because of base case n=0
    dp = [0 for x in xrange(n+1)]
    # base case
    dp[0] = 1
    for i in xrange(len(coins)):
        #for j in xrange(coins[i], n+1):     # infinite backpack
        for j in xrange(n, coins[i]-1, -1):  # 0-1 backpack
            dp[j] += dp[j-coins[i]]
        print dp
    return dp[n]
        
def make_change1_raw(m, n, coins):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 0
    return make_change1(m-1, n, coins) + make_change1(m, n-coins[m-1], coins)

def test():
    coins = [1,2,3]
    print make_change(4, coins)
    #print make_change_2d(4, coins)
    #print make_change1(len(coins), 4, coins)

    
if __name__ == '__main__':
    test()