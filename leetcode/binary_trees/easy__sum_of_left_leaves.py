# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = []
        self.dfs(root, result)
        return sum(result)

    def dfs(self, node, result, left=False):
        if node == None: return

        if not node.left and not node.right and left:
            result.append(node.val)
        
        if node.left: self.dfs(node.left, result, True)
        if node.right: self.dfs(node.right, result)
