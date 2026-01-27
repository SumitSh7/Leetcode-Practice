# Definition for a binary tree node.

from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, p, q):

        if not p and not q: 
            return True
        
        if not p or not q or p.val != q.val:
            return False

        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
    
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        """Iterative approach using a queue to check mirror symmetry."""
        if not root:
            return True
        
        queue = [(root.left, root.right)]
        
        while queue:
            left, right = queue.pop(0)
            
            if not left and not right:
                continue
            
            if not left or not right or left.val != right.val:
                return False
            
            # Compare outer and inner children
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True

