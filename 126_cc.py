import collections
import string

class Solution:
# @param start, a string
# @param end, a string
# @param dict, a set of string
# @return a list of lists of string
    def findLadders(self, start, end, dic):
        if end not in dic:
            return []

        dic.append(end)
        level = {start}
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(start)):
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

if __name__ == '__main__':
    begin ="hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().findLadders(begin, end, wordList))

