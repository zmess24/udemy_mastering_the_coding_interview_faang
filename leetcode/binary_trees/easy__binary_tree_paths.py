# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results, currentPath = [], []
        self.dfs(root, results, currentPath)
        return results
    
    def dfs(self, node, results, currentPath):
        if node == None: return
        
        currentPath.append(str(node.val))

        if not node.left and not node.right:
            path = "->".join(currentPath)
            results.append(path)
        
        leftPath = currentPath.copy()
        rightPath = currentPath.copy()

        if node.left: self.dfs(node.left, results, leftPath)
        if node.right: self.dfs(node.right, results, rightPath)