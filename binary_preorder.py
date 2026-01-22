# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                res.append(curr)

                if curr.left:
                    stack.append(curr)

                curr = curr.left


            curr = stack.pop()

            curr = curr.right

        return res
    
# Build tree from level-order list representation
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.preorder(build_tree([-26])))
    print(sol.preorder(build_tree([100,8,None,-83,None,48,None,72,None,-4])))