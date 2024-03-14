# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        results = []
        self.dfs(root, results)
        return len(results)
    
    def dfs(self, node, results):
        if node == None: return
        # Append node value to list
        results.append(node.val)
        # Explore left and then right nodes if they exist.
        if node.left: self.dfs(node.left, results)
        if node.right: self.dfs(node.right, results)
