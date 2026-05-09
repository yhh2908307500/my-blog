class TrieNode(object):
    # https://leetcode.com/articles/implement-trie-prefix-tree/#trie-node-structure
    def __init__(self):
        """
        初始化Trie节点
        """
        self.links = [None] * 26
        self.isEnd = False

    def containsKey(self, ch):
        # 检查是否包含字符ch
        return self.links[ord(ch) - ord('a')] != None

    def get(self, ch):
        # 获取字符ch对应的节点
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        # 为字符ch添加节点
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        # 标记为单词结束
        self.isEnd = True


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        向字典树中插入一个单词
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.containsKey(ch) is False:
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()

    def searchPrefix(self, word):
        # 搜索前缀
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return None
        return node


    def search(self, word):
        """
        返回单词是否在字典树中
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd


    def startsWith(self, prefix):
        """
        返回是否有单词以给定前缀开头
        :type prefix: str
        :rtype: bool
        """
        node = self.searchPrefix(prefix)
        return node is not None


        # Your Trie object will be instantiated and called as such:
        # trie = Trie()
        # trie.insert("somestring")
        # trie.search("key")