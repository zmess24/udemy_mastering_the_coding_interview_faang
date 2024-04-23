# https://www.algoexpert.io/questions/find-closest-value-in-bst
def findClosestValueInBst(tree, target, closest=float('inf')):
    if tree is None: return closest
    
    # Re-assign "closest" to lowest difference between closest & current values 
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    # 
    if target < tree.value:
        return findClosestValueInBst(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBst(tree.right, target, closest)
    else:
        return closest
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
