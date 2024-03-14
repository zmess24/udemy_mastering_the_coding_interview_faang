# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        self.dfs(root, results)
        return results[k-1]

    def dfs(self, node, results):
        if node == None: return

        # Perform In-Order DFS (left, val, right)
        if node.left: self.dfs(node.left,results)
        results.append(node.val)
        if node.right: self.dfs(node.right,results)