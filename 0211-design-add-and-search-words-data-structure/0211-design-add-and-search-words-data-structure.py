class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for w in word:
            if w in node:
                node = node[w]
            else:
                node[w] = {}
                node = node[w]
        node['$'] = {}

    def search(self, word: str) -> bool:
        nodes = [self.trie]

        for w in word:
            if not nodes:
                return False
            if w == '.':
                temp = []
                for node in nodes:
                    temp.append(node)
                nodes = []
                for node in temp:
                    for n in node.values():
                        nodes.append(n)


            else:
                temp = []
                for node in nodes:
                    temp.append(node)
                nodes = []
                for node in temp:
                    if w in node:
                        nodes.append(node[w])
        for node in nodes:
            if '$' in node:
                return True
        return False





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)