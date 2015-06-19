class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        '''
        Args: n, non-negtive number

        Return: res, number of primes
        '''
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False
        x = 2
        while x * x < n:
            if isPrime[x]:
                sq = x * x
                while sq < n:
                    isPrime[sq] = False
                    sq += x
            x += 1

        return sum(isPrime)
        
