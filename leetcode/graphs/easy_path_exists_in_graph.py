from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Convert data structure to adjacency list
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen = set()

        self.dfs(source, adj_list, seen, destination)
        return True if source in seen and destination in seen else False

    def dfs(self, vertex, graph, seen, destination):
        # Add vertex to seen
        seen.add(vertex)
        # Get connected nodes from adjacency list
        connections = graph[vertex]

        for node in connections:
            if node not in seen:
                self.dfs(node, graph, seen, destination)

