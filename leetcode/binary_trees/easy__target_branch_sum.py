# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return 0

        results = []
        self.dfs(root, 0, targetSum, results)
        return True if True in results else False



    def dfs(self, node, currentSum, targetSum, results):
        if not node: return
        currentSum = currentSum + node.val

        if node.left:
            self.dfs(node.left, currentSum, targetSum, results)
        
        if node.right:
            self.dfs(node.right, currentSum, targetSum, results)

        if not node.left and not node.right:
            ans = True if currentSum == targetSum else False
            results.append(ans)