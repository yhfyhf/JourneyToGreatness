'''
Input "/..."
Expected "/..."

Ignore more than one contious /

'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):

        stack = []
        tmp = ""
        path += "/"
        for i in range(len(path)):
            if path[i] == "/":
                if tmp == ".":
                    pass
                elif tmp == "..":
                    if stack:
                        stack.pop()
                elif  tmp == "": # //
                    pass
                else:
                    stack.append(tmp)
                tmp = ""
            else:
                tmp += path[i]

        return '/' + '/'.join(stack)

if __name__ == '__main__':
    so = Solution()
    p1 = "/a/./b/../../c/"
    p0 = "/home//"
    p2 = "/"
    p3 = "/..."
    print so.simplifyPath(p0)
    print so.simplifyPath(p2)
    print so.simplifyPath(p3)