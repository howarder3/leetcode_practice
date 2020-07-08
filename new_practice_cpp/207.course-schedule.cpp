/*
 * @lc app=leetcode id=207 lang=cpp
 *
 * [207] Course Schedule
 */

// @lc code=start
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // for(int i = 0; i < numCourses; i++){
        //     vector<bool> visited = {false}; 


        // }
        vector<unordered_set<int>> matrix(numCourses);
        for(int i=0; i < prerequisites.size();i++)
            matrix[prerequisites[i][1]].insert(prerequisites[i][0]); //course need to take

        unordered_set<int> visited;
        vector<bool> flag(numCourses, false);

        // cout<< flag.size();
        for(int i=0; i <numCourses; i++)
            if(!flag[i])
                if(DFS(matrix, visited, i, flag))
                    return false;

        return true;
    }

    bool DFS(vector<unordered_set<int>> &matrix, unordered_set<int> &visited, int b, vector<bool> &flag){
        flag[b] = true;
        visited.insert(b);

        for(auto it=matrix[b].begin(); it!=matrix[b].end(); it++)
            if(visited.find(*it) != visited.end() || DFS(matrix, visited, *it, flag))
                return true;

        visited.erase(b);
        return false;
    }
};
// @lc code=end

