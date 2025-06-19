from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        p = 0
        while q:
            l = len(q)
            p += 1 
            for _ in range(l):
                node = q.popleft()
                print(node.val)
                
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)
        return p