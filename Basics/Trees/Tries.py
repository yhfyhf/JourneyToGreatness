# Code http://blog.csdn.net/psrincsdn/article/details/8158182


class Node(object):
    def __init__(self):
        self.word = None
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            # go deeper
            node = node.children[c]


        node.word = word # mark current node as an exist word

    def search(self, word):
        # @param word, string to search
        # @return (boolean, word)
        #         boolean: found or not
        #         word: string if found, None if not input before
        node = self.root
        for c in word:
            if c not in node.children:
                return False, None
            node = node.children[c]
        return True, node.word




if __name__ == '__main__':
    t = Trie()
    words = ['abc', 'ad', 'b', 'bc', 'c', 'cat']
    for w in words:
        t.insert(w)
    print t.search('cat')
    print t.search('ca')
