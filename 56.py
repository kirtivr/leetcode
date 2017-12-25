class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return(str(self.start) + ' ' + str(self.end))

class Solution(object):
    def mergeInt(self, intv1, intv2):
        return Interval(intv1.start,max(intv1.end, intv2.end))
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # Sort the intervals by starting time
        sortIntervals = sorted(intervals, key=lambda interval : interval.start)

        mergedInts = []
        numInt = len(sortIntervals)

        i = 0
        
        while i < numInt:
            cInt = sortIntervals[i]
            
            for j in range(i+1,numInt):
                nInt = sortIntervals[j]
                
                if cInt.end >= nInt.start or cInt.end >= nInt.end:
                    cInt = self.mergeInt(cInt,nInt)
                    i = j
                    
            mergedInts.append(cInt)
            i = i + 1

        return mergedInts


il = [[1,3],[2,6],[8,10],[15,18]]
intv = [ Interval(item[0],item[1]) for item in il ]
Solution().merge(intv)

