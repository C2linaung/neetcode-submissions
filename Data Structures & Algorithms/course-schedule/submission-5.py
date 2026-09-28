class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False # already visited -> cycle
            
            if state[course] == 2:
                return True # Completed before, no need
            
            state[course] = 1 # start course
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            state[course] = 2 # finished course
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
