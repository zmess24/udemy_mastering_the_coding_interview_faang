def cycleInGraph(edges):
    # Initialize the graph from the adjacency list
    graph = {i: edges[i] for i in range(len(edges))}

    # Initialize visited and recursion stack sets
    seen = set()
    recStack = set()

    # Define the DFS function
    def dfs(node):
        # If node is already in the recursion stack, a cycle is found
        if node in recStack: return True
        # If node is already visited and not in the recursion stack, no need to process it again
        if node in seen: return False

        # Mark the node as visited and add it to the recursion stack
        seen.add(node)
        recStack.add(node)

        # Recursively visit all the connected nodes
        for connection in graph[node]:
            if dfs(connection): return True

        # Remove the node from the recursion stack
        recStack.remove(node)
        return False

    # Check for cycles in all nodes
    for node in range(len(edges)):
        if dfs(node):
            return True

    return False