from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Initialize distances dictionary with infinity
        distances = {i: float('infinity') for i in range(1, n + 1)}
        distances[k] = 0
        
        # Use a priority queue to store (distance, node)
        pq = [(0, k)]
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            # If the current distance is greater than the stored distance, skip processing
            if current_distance > distances[current_node]: continue
            
            # Explore neighbors
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                # If a shorter path to the neighbor is found, update the distance and push to the priority queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        # The result is the maximum distance in the distances dictionary
        max_distance = max(distances.values())
        
        # If the maximum distance is infinity, not all nodes are reachable
        return max_distance if max_distance != float('infinity') else -1