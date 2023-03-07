from typing import List, Optional, Tuple, Dict
from heapq import heappop, heappush, heapify
import pdb
import ast
import sys
from functools import cmp_to_key
import time

class Solution:
    def returnIntervalRangeToMergeWith(self, intervals, merge_from):
        start = intervals[merge_from][0]
        end = intervals[merge_from][1]
        if merge_from == len(intervals) - 1:
            return [merge_from, end]
        start_match = intervals[merge_from + 1][0]
        end_match = intervals[merge_from + 1][1]

        # Given interval overlaps from the left side.
        merged = [merge_from, end]
        idx = merge_from + 1
        if (start <= start_match and end >= start_match):
            # Find subsequent intervals that are also contained in the merged interval.
            merge_start = start
            merge_end = max(end, end_match)
            merged[0] = idx
            merged[1] = merge_end

            # Since `intervals` is sorted from the start element, we can only overlap from the left.
            idx += 1
            while idx < len(intervals):
                (st, en) = (intervals[idx][0], intervals[idx][1])
                if st >= merge_start and st <= merge_end:
                    merge_end = max(en, merge_end)
                    merged[0] = idx
                    merged[1] = merge_end
                    idx += 1
                else:
                    break

        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start.
        intervals = sorted(intervals, key= lambda interval: interval[0])
        out = []
        idx = 0

        while idx < len(intervals):
            to_unpack = self.returnIntervalRangeToMergeWith(intervals, idx)
            if to_unpack == []:
                break
            (merged_till_idx, end) = to_unpack
            out.append([intervals[idx][0], end])
            #print(out)
            #print(merged_till_idx)
            idx = merged_till_idx + 1
        return out


if __name__ == '__main__':
    x = Solution()
    start = time.time()
    with open('56_tc.text', 'r') as f:
        n = ast.literal_eval(f.readline())
        #print(n)
        #print(edges)
        print(x.merge(n))
    end = time.time()
    elapsed = end - start
    print(f'time elapsed: {elapsed}')