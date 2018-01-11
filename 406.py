class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        for x in people:
            out.insert(x[1],x)
        return out
    
if __name__ == '__main__':
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    print(Solution().reconstructQueue(people))

