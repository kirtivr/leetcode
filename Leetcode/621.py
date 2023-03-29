class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        numT = len(tasks)
        taskCount = {}
        taskTriples = []
        maxCount = 0
        
        for task in tasks:
            if task in taskCount:
                taskCount[task] = taskCount[task] + 1
            else:
                taskCount[task] = 1

            if taskCount[task] > maxCount:
                maxCount = taskCount[task]

        intervals = (maxCount - 1) * (n + 1)

        for task,taskC in taskCount.items():
            if taskC == maxCount:
                intervals = intervals + 1

        return intervals if intervals >= 0 else 0


if __name__ == "__main__":
    tasks = ['A','A','A','B','B','B']
    n = 2
    print(Solution().leastInterval(tasks,n))
