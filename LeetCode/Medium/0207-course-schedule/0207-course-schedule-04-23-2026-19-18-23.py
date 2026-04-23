class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white, grey, black = 1, 2, 3
        courses = [white for i in range(numCourses)]
        adj_mat = defaultdict(list)

        for now,pre in prerequisites:
            adj_mat[now].append(pre)

        def dfs(node):
            courses[node] = grey

            for nei in adj_mat[node]:
                if courses[nei] == grey:
                    return True
                elif courses[nei] == white:
                    if dfs(nei):
                        return True
            courses[node] = black
            return False

        for node in range(numCourses):
            if dfs(node):
                return False

        return True


        


        