class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[course].append(pre)

        state = [0] * numCourses
        # 0 = unvisited
        # 1 = currently visiting
        # 2 = finished

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True