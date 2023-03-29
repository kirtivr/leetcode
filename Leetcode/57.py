class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return(str(self.start) + ' ' + str(self.end))

class Solution(object):
    def mergeInts(self, intervals):
        start = 1<<30
        end = 0

        for i in intervals:
            start = min(start, i.start)
            end = max(end, i.end)
    
        return Interval(start,end)
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.append(newInterval)

        # Sort the intervals by starting time
        sortIntervals = sorted(intervals, key=lambda interval : interval.start)
        
        numInt = len(sortIntervals)
        i = 0
        toBeMerged = [newInterval]
        isInserted = False
        cInt = sortIntervals[0] if numInt > 0 else None
        
        # base case
        if cInt and cInt.start == newInterval.start and cInt.end == newInterval.end:
            nInt = newInterval
            i = 1
            while i < numInt:
                cInt = sortIntervals[i]
                
                if nInt.end >= cInt.start or nInt.end >= cInt.end:
                    k = i + 1
                    toBeMerged.append(cInt)
                    isInserted = True
                i = i + 1
            
            if isInserted:
                nInt = self.mergeInts(toBeMerged)        
                sortIntervals = [nInt] + sortIntervals[k:]
                
        else:
            print('else')
            while i < numInt:
                print('while i .. i is '+str(i))
                
                cInt = sortIntervals[i]
                startIdx = i + 1
                
                if i + 1 < numInt:
                    nInt = sortIntervals[i + 1]
                    k = i
                
                    if nInt.start == newInterval.start and nInt.end == newInterval.end:
                        if cInt.end >= nInt.start or cInt.end >= nInt.end:
                            startIdx = i
                            toBeMerged.append(cInt)
                            nInt = self.mergeInts(toBeMerged)
                            k = k + 2
                            toBeMerged = [nInt]
                            isInserted = True

                        print(nInt)

                        for j in range(i+2,numInt):
                            print('test')
                            cInt = sortIntervals[j]
#                            print(cInt)
                            if nInt.end >= cInt.start or nInt.end >= cInt.end:
                                k = j + 1
                                toBeMerged.append(cInt)
                                isInserted = True

                        if isInserted:
                            nInt = self.mergeInts(toBeMerged)
                            sortIntervals = sortIntervals[:startIdx] + [nInt] + sortIntervals[k:]
                            break
            
                    elif nInt.start > newInterval.end:
                        break

                i = i + 1

#        for i in sortIntervals:
#            print(i)
            
        return sortIntervals
#il = [[1,2],[3,5],[6,7],[8,10],[12,16]]
#it = [4,9]
#il = [[1,5]]
#it = [0, 3]
#il = [1,2],[3,5],[6,7],[8,10],[12,16]
il = [[0,5],[9,12]]
it = [7,16]
merge = Interval(it[0],it[1])
intv = [ Interval(item[0],item[1]) for item in il ]
Solution().insert(intv,merge)
