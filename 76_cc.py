import collections

class Solution:
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        print(need)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if missing == 0:
                print(s[i:j+1])
                print(need[s[i]])
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                    print(s[i])
                    if not J or j - i <= J - I:
                        I, J = i, j
                        print('window set '+s[I:J])
                print(need)
        return s[I:J]

if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    S = "acbbaca"
    T = "aba"
    S = "cabefgecdaecf"
    T = "cae"
    S = "bdab"
    T = "ab"
#    S = "aaflslflsldkalskaaa"
#    T = "aaa"
    S = "ab"
    T = "a"
    print(Solution().minWindow(S,T))

