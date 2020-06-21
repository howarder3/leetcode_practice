#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation
    def canFinish(self, numCourses, prerequisites):

        if numCourses == 1:
            return True


        # wrong, will be same!!!!!!!
        # graph = [[]]*numCourses

        graph = []
        for i in range(numCourses):
            graph.append([])

        # OR
        # graph = [[] for _ in range(numCourses)]

        visited = [0]*numCourses
        # 0 not defined
        # -1
        # 1 

        # print(graph)
        # graph[0].append(1)



        for ele in prerequisites:
            graph[ele[0]].append(ele[1])   # x course need y for prerequisites


        # print(graph)
        
        for i in range(numCourses): # check all dfs
            if not self.dfs(i, graph, visited):
                return False



        return True

    def dfs(self, x, graph, visited):
        # print(visited)
        if visited[x] == -1: # find -1 not ok -> cycle
            return False
        if visited[x] == 1: # no cycle
            return True

        visited[x] = -1 # not ok
        for j in graph[x]: # check all prereqisites, maybe no prereqisites 
            if not self.dfs(j, graph, visited):
                return False
        
        visited[x] = 1 # OK, no cycle
     
        return True
            
           
# @lc code=end

