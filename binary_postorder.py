# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        stack = [root]
        res = []
        
        while stack:
            curr = stack.pop()
            # Add to result (will be reversed later)
            res.append(curr.val)
            
            # For Modified Preorder (Root, Right, Left), push Left then Right
            # so that Right is popped first.
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        # Reverse the list to get Left, Right, Root
        return res[::-1]

    def postorderRecursive(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        dfs(root)
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
    
    print(sol.postorder(build_tree([-26])))
    print(sol.postorder(build_tree([100,8,None,-83,None,48,None,72,None,-4])))