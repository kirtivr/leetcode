class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binarySearch(numbers, target, start, end):
            if start > end:
                return None
            
            mid = start + (end-start)//2

            if numbers[mid] > target:
                return binarySearch(numbers, target, start, mid-1)
            elif numbers[mid] < target:
                return binarySearch(numbers, target, mid+1, end)
            else:
                return mid

        N = len(numbers)
        
        for i in range(N):

            curr = numbers[i]
            diff = target - curr
#            print(diff)
            found = binarySearch(numbers, diff, 0, N-1)
#            print('found = ' + str(found))
            if found != None and found != i:
                if i < found:
                    return [i+1,found+1]
                else:
                    return [found+1,i+1]
            
        return []

if __name__ == '__main__':
    l = [2,3,4]
    t = 6
    print(Solution().twoSum(l,t))

        
