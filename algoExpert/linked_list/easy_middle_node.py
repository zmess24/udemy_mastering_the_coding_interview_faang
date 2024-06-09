import math

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Create seen "list" to hold order
    seen = []
    # Create "node" variable set to LinkedList
    node = linkedList
    # While node != None:
    while node is not None:
        # Store node.value in seen list
        seen.append(node)
        # Assign node to node.next
        node = node.next
        
    # Return middle index
    middle = len(seen) // 2

    return seen[middle]
