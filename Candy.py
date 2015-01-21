class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings) <= 1:
            return len(ratings)
        candies = [1 for x in xrange(len(ratings))]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in xrange(len(ratings)-1, 0, -1):
            if ratings[i] < ratings[i-1] and candies[i] >= candies[i-1]:
                candies[i-1] = candies[i] + 1
        return sum(candies)

if __name__ == '__main__':
    s = [1,2,3,1,1]
    so = Solution()
    print so.candy(s)