import heapq
from typing import List, Optional, Tuple
import pdb
import time

class Solution:
    class Task:
        def __init__(self, name, count):
            self.name = name
            self.count = count

        # Python uses a min-heap by default.
        # Return the inverse if we want to use max-heap.
        def __lt__(self, other):
            return self.count > other.count

        def __gt__(self, other):
            return self.count < other.count

        def __repr__(self):
            return f'Task {self.name} count {self.count}'

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Process tasks in any order.
        # Gap of n seconds before processing same task twice.
        # Return minimum amount of time taken by the CPU to process all the tasks.

        # Two pools, eligible tasks and non eligible tasks.
        # Bucket sort all the tasks. Round robin guarantees the same task
        # is not processed consecutively.


        # There may be gaps where the CPU cannot work on any task
        eligible = []
        ineligible = []
        buckets = {}
        for task in tasks:
            if task in buckets:
                buckets[task] += 1
            else:
                buckets[task] = 1

        eligible = [self.Task(k, v) for k, v in buckets.items()]
        #print(eligible)
        heapq.heapify(eligible)
        #print(eligible)

        ticks = 0
        while buckets:            
            # Check if LRU ineligible task can be moved to eligible.
            #print(f'ticks = {ticks}: checking ineligible tasks, eligible = {eligible} ineligible = {ineligible} buckets = {buckets}')
            if len(ineligible) > 0:
                (lru_task, lru_time) = ineligible[0]
                if lru_time + n < ticks:
                    ineligible.pop(0)
                    heapq.heappush(eligible, self.Task(lru_task, buckets[lru_task]))
            #print(f'ticks = {ticks}: processing eligible tasks eligible = {eligible} ineligible = {ineligible} buckets = {buckets}')
            if eligible:
                task = heapq.heappop(eligible)
                #print(f'ticks = {ticks}: processed {task}')
                buckets[task.name] -= 1
                if buckets[task.name] == 0:
                    del buckets[task.name]
                else:
                    ineligible.append((task.name, ticks))
            #print(f'ticks = {ticks}: processed eligible tasks eligible = {eligible} ineligible = {ineligible} buckets = {buckets}')
            ticks += 1

        return ticks


if __name__ == '__main__':
    x = Solution()
    start = time.time()
    #tasks = ["A","A","A","B","B","B"]
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    #tasks =  ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
    n = 2
    x.leastInterval(tasks, n)
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')