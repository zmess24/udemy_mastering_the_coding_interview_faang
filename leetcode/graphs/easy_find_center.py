class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set([])

        for nodes in edges:
            # Seperate Nodes
            n1, n2 = nodes[0], nodes[1]

            if n1 in seen: 
                return n1
            elif n2 in seen:
                return n2
            else:
                seen.add(n1)
                seen.add(n2)