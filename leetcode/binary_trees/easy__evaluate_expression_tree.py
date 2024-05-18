# https://www.algoexpert.io/questions/evaluate-expression-tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluateExpressionTree(tree, ans=0):
    if not tree: return
        
    if tree.value == -1:
        ans = evaluateExpressionTree(tree.left, ans) + evaluateExpressionTree(tree.right, ans)
        return ans
    elif tree.value == -2:
        ans = evaluateExpressionTree(tree.left, ans) - evaluateExpressionTree(tree.right, ans)
        return ans
    elif tree.value == -3:
        ans = int(evaluateExpressionTree(tree.left, ans) / evaluateExpressionTree(tree.right, ans))
        return ans
    elif tree.value == -4:
        ans = evaluateExpressionTree(tree.left, ans) * evaluateExpressionTree(tree.right, ans)
        return ans
    else:
        return tree.value
    
    
