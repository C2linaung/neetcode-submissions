class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)
        state = [0] * numCourses # 1 for in progress, 2 for completed

        def dfs(course):
            if state[course] == 1:
                return False # already in progress -> cycle
            
            if state[course] == 2:
                return True # already complete, no need check further
            
            state[course] = 1 # mark starting
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            state[course] = 2 # mark completition

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True