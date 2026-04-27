class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # iterative approach

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        print(graph)

        visited = set()
        stack = [source]
        found = False

        while stack:
            node = stack.pop()
            if node == destination:
                found =  True
                break
            
            if node not in visited:
                visited.add(node)
                
                for i in reversed(graph[node]):
                    stack.append(i)
        
        return found

