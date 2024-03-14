# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        results = []
        self.dfs(root, results, [], 0)
        return sum(results)

    def dfs(self, node, results, curr, depth):
        if node == None: return

        curr.append(str(node.val))

        if not node.left and not node.right:
            num = "".join(curr)
            results.append(int(num))
        
        depth = depth + 1

        if node.left:
            self.dfs(node.left, results, curr, depth)
        if node.right: 
            print(curr)
            self.dfs(node.right, results, curr[:depth], depth)