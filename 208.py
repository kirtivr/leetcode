class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """        
        self.trie = None
        self.node = {}
        letter = 'a'

        while letter <= 'z':
            self.node[letter] = None
            letter = chr(ord(letter)+1)
        self.node['$'] = False

        self.trie = dict(self.node)
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        N = len(word)
        curr = self.trie
        for i in range(N):
            ch = word[i]
            if curr[ch] == None:
                curr[ch] = dict(self.node)
            if i == N-1:
                curr[ch]['$'] = True
            curr = curr[ch]
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        N = len(word)
        curr = self.trie
        
        for i in range(N):
            ch = word[i]
            if curr[ch] == None:
                return False
            if i == N-1 and curr[ch]['$'] == True:
                return True
            curr = curr[ch]

        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        N = len(prefix)
        curr = self.trie
        
        for i in range(N):
            ch = prefix[i]
            if curr[ch] == None:
                return False
            #print(curr)
            curr = curr[ch]

        return True


# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    obj = Trie()
    word = "banana"
    obj.insert(word)
    obj.insert('nanako')
    param_2 = obj.search(word+'e')
    print(param_2)
    prefix = 'nan'
    param_3 = obj.startsWith(prefix)
    print(param_3)
