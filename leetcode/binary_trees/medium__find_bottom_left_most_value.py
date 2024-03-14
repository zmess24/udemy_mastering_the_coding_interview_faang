class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return root

        queue = [root]
        currentNode = None

        while (len(queue) > 0):
            currentNode = queue.pop(0)
            
            if currentNode.right: queue.append(currentNode.right)
            if currentNode.left: queue.append(currentNode.left)

        return currentNode.val
