# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []
    dfs(root, 0, result)
    return result

def dfs(node, branchSum, results):
    if node:
        branchSum += node.value
        
        if node.left:
            dfs(node.left, branchSum, results)
        if node.right:
            dfs(node.right, branchSum, results)

        if (node.left == None and node.right == None):
            results.append(branchSum)
    else:
        return
        
