class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        """
        greedy method
        for each idx, judge whether it could move to the next one
        @ jump: the available jump steps
        can be viewed as dp too
        """
        if not A:
            return 0
        jump = A[0]
        for i in xrange(1, len(A)):
            if jump_len > 0:
                jump -= 1
                jump = max(jump, A[i])
            else: # cannot jump forward
                return False
        return True