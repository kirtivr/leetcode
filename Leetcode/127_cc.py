from collections import deque

class Solution(deque):

    def ladderLength(self, begin, end, wordList):

        def construct_dect(word_list):
            d = {}

            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) +[word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin,1)]), set()

            while queue:
                word,steps = queue.popleft()

                visited.add(word)

                if word == end:
                    return steps

                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]

                    neigh_words = dict_words.get(s, [])

                    for neigh in neigh_words:
                        if neigh not in visited:
                            queue.append((neigh, steps + 1))

            return 0

        if end not in wordList:
            return 0

        d = construct_dect(wordList + [ begin, end ])

        return bfs_words(begin, end, d)


if __name__ == '__main__':
    begin ="hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().ladderLength(begin, end, wordList))
                

