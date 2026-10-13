class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)
        state = [0 for _ in range(numCourses)] # 1: in progress, 2: complete

        def dfs(course):
            if state[course] == 1:
                return False # cycle is detected
            
            if state[course] == 2:
                return True # complete the course before already
            
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