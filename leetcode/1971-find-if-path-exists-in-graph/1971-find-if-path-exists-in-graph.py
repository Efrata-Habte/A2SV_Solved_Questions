class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for v,e in edges:
            graph[e].append(v)
            graph[v].append(e)

        visited = set()

        def dfs(node, visited,destination):
            if node == destination:
                return True

            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei,visited,destination):
                        return True

            return False
        
        return dfs(source, visited, destination)