class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ''' we need an 1 to 1 match here. so 2 map is needed.
        case 1: src and dst not in map, add them
        case 2: not in map or mismatch, so we use dict's get method (not in map
        return None, mismatch return other element)
        '''
        src_map, dst_map = {}, {}
        for i in range(len(s)):
            if s[i] not in src_map and t[i] not in dst_map:
                src_map[s[i]] = t[i]
                dst_map[t[i]] = s[i]
            elif src_map.get(s[i]) != t[i] or dst_map.get(t[i]) != s[i]:
                return False
        return True
