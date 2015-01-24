class Solution:

    def __justify(self, words, L):
        sep_num = len(words) - 1
        if not sep_num:
            return words[0] + ' ' * (L-len(words[0]))
        sep = (L - sum(len(w) for w in words)) / sep_num
        rem = (L - sum(len(w) for w in words)) - sep*sep_num
        buf = [[] for x in xrange(len(words))]
        for i in xrange(len(words)-1):
            buf[i].append(words[i] + ' ' * sep )
        buf[-1].append(words[-1])
        for i in xrange(len(words)-1):
            if rem <= 0:
                break
            buf[i].append(' ')
            rem -= 1
            
        return ''.join([''.join(buf[i]) for i in xrange(len(buf))])

    
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        res = []
        start = 0
        curr = 0
        for i in xrange(len(words)):
            if curr + len(words[i]) > L:
                res.append(self.__justify(words[start:i], L))
                start = i
                curr = len(words[i]) + 1
            else:
                curr += len(words[i]) + 1

        lastline = ' '.join(words[start:])
        padding = ' ' * (L - len(lastline))
        res.append(' '.join(words[start:])+ padding)
        return res


if __name__ == '__main__':
    so = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]

    ws = ["What","must","be","shall","be."]
    print so.fullJustify(ws, 12)