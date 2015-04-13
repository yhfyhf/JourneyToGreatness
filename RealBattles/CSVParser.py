# -*- coding: utf-8 -*-

"""
http://www.1point3acres.com/bbs/thread-124107-1-1.html
http://www.mitbbs.com/article_t/JobHunting/32735761.html

Ask: can we assume all string are valid

#1. neither ',' nor '"': add to res
#2. ',': add to res if in single_quote or double_quote state, else parse as '|'
#3. '"': this is the last char or successor is not '"', reverse single_quote state
#4. '"': this is not the last char and successor is '"', add '"' to res, skip one i
"""

class CSVParser:
    # def __init__(self, data):
    #     self.data = data
    def parse_line(self, ss):
        single_q = False
        double_q = False
        res = ""
        N = len(ss)
        i = 0
        while i < N:
            # ignore space ? depends on requirements
            if ss[i] != '"' and ss[i] != ',':
                res += ss[i]
            elif ss[i] == ',':
                if single_q or double_q:
                    res += ss[i]
                else:
                    res += '|'
            else: # ss[i] == '"'
                if i == N - 1 or ss[i+1] != '"':
                    single_q = not single_q
                if i < N - 1 and ss[i+1] == '"':
                    double_q = not double_q
                    res += '"'
                    i += 1
            i += 1
        return res

    def test(self):
        lines = ['John,Smith,john.smith@gmail.com,Los Angeles,1',
                 'Jane,Roberts,janer@msn.com,"San Francisco, CA",0',
                 '"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1',
                 '"""Alexandra Alex"""',
                 'a, a"b","a"b',
                 '"aaaa""bb""a"'
        ]
        for l in lines:
            print self.parse_line(l)


if __name__ == '__main__':
    p = CSVParser()
    p.test()

                
        
