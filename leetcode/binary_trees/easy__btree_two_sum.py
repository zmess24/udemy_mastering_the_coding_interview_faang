# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = [root]
        hashMap = {}
        currentNode = None

        while len(queue):
            currentNode = queue.pop(0)

            if currentNode.val in hashMap:
                return True
            else:
                key = k - currentNode.val
                hashMap[key] = currentNode.val
            
            if currentNode.left: queue.append(currentNode.left)
            if currentNode.right: queue.append(currentNode.right)            
        
        return False
            