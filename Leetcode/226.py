import heapq
from typing import List, Optional, Tuple
import pdb
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None):
            return root

        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp

        return root

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