class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        cnt = [0 for i in range(32)]
        res = 0
        for i in range(32):
            for j in A:
                if (j>>i) & 1:
                    cnt[i] += 1;
                    
            res |= (cnt[i]%3) << i;
        return res