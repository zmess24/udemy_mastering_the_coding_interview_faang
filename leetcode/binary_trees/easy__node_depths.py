def nodeDepths(root):
    result = []
    dfs(root, 0, result)
    return sum(result)

def dfs(node, depth, result):
    if node == None: return 0

    result.append(depth)
    
    dfs(node.left, depth+1, result)
    dfs(node.right, depth+1, result)
    
    return result
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
