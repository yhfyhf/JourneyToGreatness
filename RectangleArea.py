class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        width, height = self.getCross(A, C, E, G), self.getCross(B, D, F, H)
        return (C - A) * (D - B) + (G - E) * (H - F) - width * height

    def getCross(self, x1, x2, X1, X2):
        # not overlapped
        if x1 >= X2 or x2 <= X1:
            return 0
        # make sure the smaller pair is x1, x2
        if x1 >= X1:
            x1, x2, X1, X2 = X1, X2, x1, x2
        # covered
        if x2 >= X2: #x1 <= X1 and x2 >= X2
            return X2 - X1
        # overlapped, merge two case into one
        return x2 - X1
