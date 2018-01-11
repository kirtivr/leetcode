class Solution(object):
    def numSquares(self, n):
        sums = {0}
        while n not in sums:
            sums = {sum + i*i
                    for sum in sums
                    for i in range(1, int((n - sum)**0.5 + 1))}
            print(sums)
        print(sums)
        return min(sums)

if __name__ == '__main__':
    print(Solution().numSquares(12))
