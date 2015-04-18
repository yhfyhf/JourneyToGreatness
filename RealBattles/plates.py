class Node():
    def __init__(self):
        self.children = {}

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            # the path exist
            node = node.children[c]

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

class Plate:
    def __init__(self, dictionary):
        # @param dictionary: a list of words
        self.__trie = Trie()
        for word in dictionary:
            word = ''.join(sorted(word))
            self.__trie.insert(word)
            
    def get_word(self, plate):
        # @param plate: a string contains letter and numbers
        # @return word: the shortest word contain all letters in plate
        query = []
        for c in plate:
            if ord(c) <= ord('z') and ord(c) >= ord('a'):
                query.append(c)
        query.sort()
        query = ''.join(query)
        return self.__trie.search(query)
    

if __name__ == '__main__':
    d = ['dog', 'cat', 'foo', 'bar', 'baz']
    querys = ['d', 'ct', 'fo', 'bard', 'bar']
    plate = Plate(d)
    for q in querys:
        print plate.get_word(q)

