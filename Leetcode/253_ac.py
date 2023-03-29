# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return(str(self.start) + ' ' + str(self.end))

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        # Sort the intervals by starting time and store those
        start = []
        for i in intervals:
            start.append(i.start)

        start.sort()
        # Sort the intervals by end time and store those as well
        end = []
        for i in intervals:
            end.append(i.end)
        end.sort()
#        print(end)
        
        numInt = len(start)
        sp, ep = 0,0
        numRooms = available = 0
        
        while sp < numInt:
            if start[sp] < end[ep]:
#                print(str(start[sp]) + ' ' + str(end[ep]))
                if available == 0:
                    numRooms = numRooms + 1
                else:
                    available -= 1
                sp += 1
            else:
                available += 1
                ep += 1

        return numRooms

#il = [[7,10],[2,4]]
il = [[0, 30],[5, 10],[15, 20]]
#il = [[0,10],[15,20],[10,25],[20,30],[5,15]]
#il = [[1,8],[4,6]]
#il = [[9,10],[4,9],[4,17]]
intv = [ Interval(item[0],item[1]) for item in il ]
print(Solution().minMeetingRooms(intv))

