class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # iterative approach BFS

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        print(graph)

        visited = set()
        queue = deque()
        queue.append(source)
        found = False

        while queue:
            node = queue.popleft()
            if node == destination:
                found =  True
                break
            
            if node not in visited:
                visited.add(node)
                
                for i in (graph[node]):
                    queue.append(i)
        
        return found

