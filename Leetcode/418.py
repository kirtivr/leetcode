class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # Check sentence
        wordLens = []
        for word in sentence:
            wordLens.append(len(word))

        startEnd = {}
        totalWords = len(sentence)
        
        for i in range(totalWords):
            remSpace = cols
            j = i 
            fittedWords = 0

            while True:
                remSpace = remSpace - wordLens[j]

                if remSpace > 0:
                    remSpace = remSpace - 1 # space
                    fittedWords = fittedWords + 1
                elif remSpace == 0 or remSpace == 1:
                    fittedWords = fittedWords + 1
                    j = (j + 1) % (totalWords)
                    break
                else:
                    break
                j = (j + 1) % (totalWords)

            startEnd[i] = (fittedWords, j)

        print(startEnd)
        numWords = 0
        numSent = 0
        currWord = 0
        
        for i in range(rows):
            numWords = numWords + startEnd[currWord][0]
            currWord = startEnd[currWord][1]

        numSent = int(numWords / totalWords)

        return numSent


if __name__ == '__main__':
    inp1 = ["hello","world"]
    inp2 = [2,8]
    print('woah?')
    print(Solution().wordsTyping(inp1,inp2[0],inp2[1]))
