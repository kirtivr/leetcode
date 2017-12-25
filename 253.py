# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return(str(self.start) + ' ' + str(self.end))

class Solution(object):
    def intersects(self, s, e):
        if s.end <= e.start:
            print('['+str(s) + '] and 1 ['+ str(e) + '] dont intersect')
            return False
        elif s.start >= e.end:
            print('['+str(s) + '] and 2 ['+ str(e) + '] dont intersect')
            return False
        print('['+str(s) + '] and ['+ str(e) + '] intersect')
        return True

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        # Sort the intervals by starting time
        stSort = sorted(intervals, key=lambda interval : interval.start)
        endSort = sorted(intervals, key=lambda interval : interval.end)
        
        totalAvail = 1
        currAvail = 0
        
        numInt = len(intervals)

        stPtr = 0
        endPtr = 0

        seen = {}

        while stPtr < numInt and endPtr < numInt:
            sInt = stSort[stPtr]
            eInt = endSort[endPtr]

            seen[(sInt.start,sInt.end)] = True
            
            if (sInt.start == eInt.start and sInt.end == eInt.end) or ((eInt.start,eInt.end) in seen):
                endPtr = endPtr + 1
                continue

            if self.intersects(sInt,eInt):
                if currAvail == 0:
                    totalAvail = totalAvail + 1
                    currAvail = 0
                else:
                    print('cast '+str(sInt)+ ', '+str(eInt))
                    currAvail = currAvail - 1
            else:
                ti = endPtr + 1
                while ti < numInt:
                    temp = endSort[ti]

                    if not self.intersects(sInt,temp):
                        ti = ti + 1
                    else:
                        if currAvail == 0:
                            totalAvail = totalAvail + 1
                            currAvail = 0
                        else:
                            print('cast '+str(sInt)+ ', '+str(eInt))
                            currAvail = currAvail - 1

                        ti = ti + 1
                currAvail = currAvail + 1

                # something freed up
                if sInt.start > eInt.start: 
                    endPtr = endPtr + 1
                else:
                    stPtr = stPtr + 1
                    
            stPtr = stPtr + 1
            
        return totalAvail

#il = [[7,10],[2,4]]
il = [[0, 30],[5, 10],[15, 20]]
#il = [[0,10],[15,20],[10,25],[20,30],[5,15]]
#il = [[1,8],[4,6]]
#il = [[9,10],[4,9],[4,17]]
intv = [ Interval(item[0],item[1]) for item in il ]
print(Solution().minMeetingRooms(intv))
