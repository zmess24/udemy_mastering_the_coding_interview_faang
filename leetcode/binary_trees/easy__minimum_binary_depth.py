# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
            
        depthTotals = []
        self.dfs(root, 1, depthTotals)
        return min(depthTotals)

    def dfs(self,node, depth, depthTotals):
        if node:
            if node.left: 
                self.dfs(node.left, depth+1, depthTotals)
            if node.right: 
                self.dfs(node.right, depth+1, depthTotals)

            if not node.left and not node.right:
                depthTotals.append(depth)
        else:
            return

    
