
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        end = len(A) - 1
        for i in range(len(A)-1, -1, -1):
            if A[i] == elem:
                print "end",end
                A[i], A[end] = A[end], A[i]
                end -= 1
        return end+1

if __name__ == '__main__':
    so = Solution()
    A = [4,5]
    e = 4
    print so.removeElement(A,e)

            