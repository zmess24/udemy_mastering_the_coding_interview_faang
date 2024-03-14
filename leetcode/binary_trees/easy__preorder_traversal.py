# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, node, result):
        if node == None: return

        result.append(node.val)

        if (node.left):
            self.dfs(node.left, result)

        if (node.right):
            self.dfs(node.right, result)