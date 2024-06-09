# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    seen = []
    dfs(tree, seen, k)
    return seen[len(seen)-k]

# Define dfs function(node, values, k) (in order):
def dfs(node, seen, k):
    if not node: return seen

    # dfs on left node
    if node.left: dfs(node.left, seen, k)
    # Add current node to list
    seen.append(node.value)
    # dfs on right node
    if node.right: dfs(node.right, seen, k)

    return seen
