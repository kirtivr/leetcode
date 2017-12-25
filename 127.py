class Solution(object):
    def getChange(self, words, word, wd):
        change = 0
        for i in range(len(word)):
            c = word[i]
            ch = wd[i]
            
            if c != ch:
                change += 1
                if change > 1:
                    break
        return change
            
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        words = {}

        for word in wordList:
            words[word] = []
            for wd,nn in words.items():
                change = self.getChange(words,word,wd)
                if change == 1:
                    words[word].append(wd)
                    words[wd].append(word)
                    

        queue = []
        
        for wd, nn in words.items():
            change = self.getChange(words,word,wd)
            if change == 1:
                queue.append((wd,1))


        visited = {}
        length = 0

        while len(queue) > 0:
            toVisit,edges = queue.pop(0)
            
            if toVisit not in visited:
                print(toVisit + str(edges))
                visited[toVisit] = edges + 1

                if toVisit == endWord:
                    print(toVisit)
                    return edges + 1
                    
                for nn in words[toVisit]:
                    queue.append((nn,edges+1))

        return 0
            
if __name__ == '__main__':
    begin ="hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().ladderLength(begin, end, wordList))
                
