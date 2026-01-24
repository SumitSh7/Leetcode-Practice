# Definition for a binary tree node.
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

         
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return False
        
        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root