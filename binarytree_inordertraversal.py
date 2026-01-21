# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

        res = []
        
        def traverse(node):
            if not node:
                return
            
            # Left -> Visit -> Right
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
            
        traverse(root)
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
    
    print(sol.inorderTraversal(build_tree([-26])))
    print(sol.inorderTraversal(build_tree([100,8,None,-83,None,48,None,72,None,-4])))
    print(sol.inorderTraversal(build_tree([97,78,32,80,79,29,-29,None,45,None,-20,None,-20,13,None,97,-41,-100,94,None])))
    print(sol.inorderTraversal(build_tree([73,-55,76,None,71,-71,72,None,-63,None,-34,None,-9,None,-98,-19,-87,-83,63,-70,None,77,None,-36,None,-77,6,None,29,None])))
    print(sol.inorderTraversal(build_tree([-72,11,-94,None,3,76,None,51,71,19,None,89,-62,None,-13,84,None,-66,55,-10,None,-99,-55,5,-40,20,None,-6,None,-60,None,39,None,38,-95,57,None,40,None,38])))
    print(sol.inorderTraversal(build_tree([52,None,13,None,52,None,47,None,-75,-16,None,-10,None,7,99,10,None,20,None,15,-100,None,-37,67,0,-86,None,-96,25,None,68,-20,25,-28,-94,None,37,-22,None,65,-72,-24,None,90,19,None,86,-40,None,-7])))
    print(sol.inorderTraversal(build_tree([36,None,9,None,62,66,None,56,97,55,None,51,-21,None,81,62,-88,None,-67,-40,None,-61,None,-79,98,None,37,-42,-60,-61,None,-70,-47,None,67,90,22,27,None,88,-34,None,43,67,-10,None,73,None,42,None,-21,1,-46,-58,None,33,None,72,-20,None,82,-23,None,87,27,None,-34,62,60,None,-49,None,-74,-5,None,49,None,-85,36,5,60,None,71,59,57,None,-68,55,None,-36,11,-18,None,-87,-91,None,-74,None,-17,-25])))
    print(sol.inorderTraversal(build_tree([9,None,34,6,-17,None,-94,-54,60,-99,-30,None,100,None,-16,57,None,-90,-11,None,-17,None,-72,None,70,None,56,None,4,-65,None,-75,None,20,71,None,1,-7,-54,30,None,66,None,59,98,None,31,78,-7,-87,None,-4,25,96,-56,None,39,-63,None,-95,None,-37,80,None,-52,None,-85,31,None,51,None,3,82,None,-50,None,95,60,None,49,75,None,91,36,None,-27,None,-87,-13,None,96,None,87,None,19,None,-96,-69,None,-2])))
