from collections import deque
import copy

class Solution(deque):

    def findLadders(self, begin, end, wordList):

        def construct_dect(word_list):
            d = {}

            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) +[word]
            return d

        def trace(word, parent, paths):
            current = word
#            print(current)
            print(parent)
            
            while parent[current] != None:
                pps = parent[current]

                if len(pps) > 1:
                    old_paths = paths
                    paths = None
#                    print(pps)
                    while len(pps) > 0:
                        pp = pps.pop()
                        for path in old_paths:
                            path.appendleft(pp)
                            
                        follow = trace(pp, parent, copy.deepcopy(old_paths))

                        for path in old_paths:
                            path.popleft()

                        if paths:
                            paths.extend(follow)
                        else:
                            paths = follow
                            
                    return paths
                else:
                    for path in paths:
                        path.appendleft(pps[0])
                current = pps[0]

            return paths
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin,1)]), set()
            parent = {begin: (None,0)}
            found = False
            
            while queue:
                word,steps = queue.popleft()

                visited.add(word)

                if word == end:
                    found = True

                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]

                    neigh_words = dict_words.get(s, [])

                    for neigh in neigh_words:
                        if neigh not in visited:
                            queue.append((neigh, steps + 1))
                            
                        if neigh in parent and steps < parent[neigh][1]:
                            parent[neigh] = ([word], steps)
                        elif neigh in parent and steps == parent[neigh][1] and word not in parent[neigh][0]:
                            parent[neigh][0].append(word)
                        elif neigh not in parent:
                            parent[neigh] = ([word], steps)
            if found:
                parent = { key:value[0] for key,value in parent.items() }
                paths = trace(end, parent, [deque([end])])
                paths = [list(p) for p in paths]
                return paths
            
            return 0

        if end not in wordList:
            return 0

        d = construct_dect(wordList + [ begin, end ])

        return bfs_words(begin, end, d)

if __name__ == '__main__':
    begin ="hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().findLadders(begin, end, wordList))
