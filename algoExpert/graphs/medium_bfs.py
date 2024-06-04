# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        seen = set()

        while len(queue):
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            seen.add(currentNode.name)

            for i in range(len(currentNode.children)):
                connection = currentNode.children[i]
                if connection.name not in seen:
                    queue.append(connection)
            
        return array
