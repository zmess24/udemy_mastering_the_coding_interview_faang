def twoColorable(edges):
    # Convert edges into adjacency list
    graph = {i: edges[i] for i in range(len(edges))}
    # Init seen dict
    seen = {}
    # Color Constants
    BLACK, RED = 0, 1
    
    # DFS function declaration
    def dfs(node, prevColor = BLACK):
        # Assign color opposite currentNode
        seen[node] = RED if prevColor == BLACK else BLACK
        # Grab connections for node from graph
        for connection in graph[node]:
            # If connection not in set:
            if connection not in seen:
                return dfs(connection, seen[node])
            elif seen[connection] == seen[node]:
                return False
                
        return True
                
    if dfs(0): return True
    
    return False
