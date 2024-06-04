# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Implement DFS
    # Init seen set, currentNode = D1.ancestor, and yca = false
    seen = set()
    currentNode = descendantOne
    youngestCommonAncestor = False
    
    # Iterate through D1 using while D1 has ancestor
    while currentNode is not None:
        # Add node name to seenSet
        seen.add(currentNode.name)
        # Assign currentNode to node.ancestor
        currentNode = currentNode.ancestor

    # Reset currentNode to D2
    currentNode = descendantTwo
    
    # Iterate through D2 using while D2 has ancestor
    while currentNode is not None:
        # If node.name in seen set
        if currentNode.name in seen:
            # Assign yca = node.name
            youngestCommonAncestor = currentNode
            # break iteration
            break
        else:
            # Assign currentNode to node.ancestor
            currentNode = currentNode.ancestor

    return youngestCommonAncestor
