class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestor_set = [set() for i in range(n)]

        for u,v in edges:
            graph[u].append(v)

        def dfs(curr,start):
            for nei in graph[curr]:
                if start not in ancestor_set[nei]:
                    ancestor_set[nei].add(start)
                    dfs(nei,start)

        for i in range(n):
            dfs(i,i)

        return [sorted(list(i)) for i in ancestor_set]