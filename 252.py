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
        # Sort the intervals by starting time
        sortIntervals = sorted(intervals, key=lambda interval : interval.start)

        maxLen = 0
        numInt = len(sortIntervals)
        
        for i in range(numInt):
            cInt = sortIntervals[i]
            overlap = 1
            for j in range(i+1,numInt):
                pInt = sortIntervals[j]
                if cInt.end <= pInt.start:
                    continue
                else:
                    overlap = overlap + 1
            maxLen = max(overlap, maxLen)

        return maxLen

il = [[7,10],[2,4]]
intv = [ Interval(item[0],item[1]) for item in il ]
print(Solution().minMeetingRooms(intv))
