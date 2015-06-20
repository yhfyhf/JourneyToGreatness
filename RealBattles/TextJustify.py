
def fullJustify(words, maxWidth):
    res = []
    i = 0
    while i < len(words):
        j = i + 1
        curr_len = len(words[i])
        while j < len(words) and curr_len + 1 + len(words[j]) <= maxWidth:
            curr_len += len(words[j]) + 1
            j += 1
        n = j - i - 1
        spaces = maxWidth - curr_len + n if j < len(words) else n
        this_line = words[i]
        
        for w in range(i + 1, j):
            this_line +=  ' '* (spaces/n + (w-i <= spaces%n))
            this_line += words[w]
        res.append(this_line)
        i = j
                                 
    return res

def justify(words, maxWidth):
    res = []
    i = 0
    while i < len(words):
        curr_len = len(words[i])
        j = i + 1
        while j < len(words) and curr_len + 1 + len(words[j]) <= maxWidth:
            curr_len += len(words[j]) + 1
            j += 1
        nspaces = j - i - 1
        spaces = maxWidth - curr_len + nspaces if j < len(words) else nspaces
        # assemble the line
        line = words[i]
        for w in range(i + 1, j):
            line += ' ' * (spaces/nspaces + (w - i <= spaces % nspaces))
            line += words[w]
        res.append(line)
        i = j
    return res

words = ["This", "is", "an", "example", "of", "text", "justification.", "aa", "b"]
maxWidth = 16
#for line in fullJustify(words, maxWidth):
for line in justify(words, maxWidth):
    print line
