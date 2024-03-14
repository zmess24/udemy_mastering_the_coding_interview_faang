# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, node, result):
        if node == None: return

        if node.left:
            self.dfs(node.left, result)
        
        result.append(node.val)

        if node.right:
            self.dfs(node.right, result)
        
