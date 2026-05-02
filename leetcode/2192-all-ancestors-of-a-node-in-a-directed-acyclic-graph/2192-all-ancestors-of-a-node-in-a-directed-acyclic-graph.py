from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            
        ancestors_set = [set() for _ in range(n)]
        
        def dfs(curr, start):
            for neighbor in graph[curr]:
                # If 'start' is not already in the neighbor's ancestor set, add it and continue
                if start not in ancestors_set[neighbor]:
                    ancestors_set[neighbor].add(start)
                    dfs(neighbor, start)
                    
        for i in range(n):
            dfs(i, i)
            
        return [sorted(list(s)) for s in ancestors_set]