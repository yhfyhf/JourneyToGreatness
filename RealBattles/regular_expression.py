'''
Regular expression matching

isMatch(“aa”,”a”) → false
isMatch(“aa”,”aa”) → true
isMatch(“aaa”,”aa”) → false
isMatch(“aa”, “a*”) → true
isMatch(“aa”, “.*”) → true
isMatch(“ab”, “.*”) → true
isMatch(“aab”, “c*a*b”) → true

'''

def is_match2(s, p):
    # @s: string
    # @p: string
    # @return: Bool
    if len(p) == 0:
        return len(s) == 0
    # next char is not *
    if len(p) == 1 or p[1] != '*':
        return (len(s) != 0 and (p[0] == s[0] or p[0] == '.')) and is_match(s[1:], p[1:])
    # next char is *
    while len(s) != 0 and (p[0] == s[0] or p[0] == '.'):
        if is_match(s, p[2:]):
            return True
        s = s[1:]
    return is_match(s, p[2:])
        
def is_match(s, p):
    # @s: string
    # @p: string
    # @return: Bool
    if len(p) == 0:
        return len(s) == 0
    # next char is not *
    if len(p) == 1 or p[1] != '*':
        if len(s) == 0 or (p[0] != s[0] and p[0] != '.'):
            return False
        # same or match .
        return is_match(s[1:], p[1:])
  
    # next char is *
    return (len(s) != 0 and (p[0] == s[0] or p[0] == '.') and is_match(s[1:], p)) or is_match(s, p[2:])

    if len(s) == 0 or (p[0] != s[0] and p[0] != '.'):
        return is_match(s, p[2:])
    return is_match(s[1:], p) or is_match(s, p[2:])

def is_match3(s, p):
    if len(p) == 0:
        return len(s) == 0
    if len(p) == 1 or p[1] != '*':
        
            

print is_match("kasa", "k*")
print is_match("", "a")
print is_match("aa", "a")
print is_match("ab", ".*")
print is_match("aaa", "aa")
print is_match("aa", "a*")
print is_match("aa", "b*")
print is_match("aab", "c*a*b")
