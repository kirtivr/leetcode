class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        numH = len(heights)
        
        maxA = 0
        area = 0
        stk = []
        
        for i in range(numH):
            el = heights[i]
            area = 0
            
            if len(stk) == 0:
                print(1)
                stk.append((el,i))
                area = el
            else:
                (top,topIdx) = stk.pop()

                if top > el:
                    print(2)
                    idx = topIdx
                    append = True
                    while top > el:
                        idx = topIdx
                        numEls = i - topIdx + 1
                        elArea = el * numEls
                        topArea = top * (numEls - 1)
                        elArea = elArea if elArea > topArea else topArea
                        area =  elArea if elArea > area else area 
                        if len(stk) > 0:
                            (top,topIdx) = stk.pop()
                        else:
                            append = False
                            break
                        
                    if append:
                        print(3)
                        stk.append((top, topIdx))
                    if el != top:
                        stk.append((el,idx))
                    
                elif top < el:
                    print(4)
                    topArea = top * (i - topIdx + 1)
                    print("4 top ar is "+str(topArea))
                    area = topArea if el < topArea else el
                    stk.append((top,topIdx))
                    stk.append((el,i))
                    
                elif top == el:
                    print(5)
                    topArea = top * (i - topIdx + 1)
                    area = topArea
                    stk.append((top,topIdx))
            
            if area > maxA:
                maxA = area
            print(stk)
            print(maxA)
        
        while len(stk) > 0:
            (top,topIdx) = stk.pop()
            area = top * (numH - topIdx)
            if area > maxA:
                maxA = area
                
        return maxA

if __name__ == '__main__':
#    nums = [2,1,5,6,2,3]
    #nums = [0,0,0,0,0,0,0,0,2147483647]
#    nums = [2,1,2]
#    nums = [5,4,1,2]
#    nums = [1,2,3,4,5]
#    nums = [4,2,0,3,2,4,3,4]
#    nums = [3,6,5,7,4,8,1,0]
    nums = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
    print(Solution().largestRectangleArea(nums))
