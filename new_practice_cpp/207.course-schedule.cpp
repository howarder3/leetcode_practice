/*
 * @lc app=leetcode id=207 lang=cpp
 *
 * [207] Course Schedule
 */

// @lc code=start

// https://leetcode.com/problems/course-schedule/discuss/58709/BFS(Topological-Sort)-and-DFS(Finding-cycle)-by-C%2B%2B
/*
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // prerequisites = [[1,0],[0,1]]     [current, pre]
        // for(int i = 0; i < numCourses; i++){
        //     vector<bool> visited = {false}; 


        // }
        vector<unordered_set<int>> matrix(numCourses); // numCourses 個 unordered_set<int>
        for(int i=0; i < prerequisites.size();i++)
            matrix[prerequisites[i][1]].insert(prerequisites[i][0]); // course need to take
            // matrix[pre].insert(current);
            // pre: current1, current2, current3

        unordered_set<int> visited;
        vector<bool> flag(numCourses, false);

        // cout<< flag.size();
        for(int i=0; i <numCourses; i++)
            if(!flag[i]) // not checked
                if(DFS(matrix, visited, i, flag)) // DFS true, cycle found
                    return false;

        return true;
    }

    bool DFS(vector<unordered_set<int>> &matrix, unordered_set<int> &visited, int b, vector<bool> &flag){
        flag[b] = true; // checked b flag
        visited.insert(b); // seen b, if double seen -> false

        for(auto it=matrix[b].begin(); it!=matrix[b].end(); it++) // seen all this course prerequisites
            if(visited.find(*it) != visited.end() || DFS(matrix, visited, *it, flag))
                // found in visited -> DFS true
                // DFS found(true)
                return true;

        visited.erase(b); //delete seen
        return false;
    }
};

// vector<unordered_set<int>> &matrix 
// unordered_set<int> &visited 
// int b
// vector<bool> &flag
*/

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites)
    {
        vector<unordered_set<int>> matrix(numCourses); // save this directed graph
        for(int i = 0; i < prerequisites.size(); ++ i)
            matrix[prerequisites[i][1]].insert(prerequisites[i][0]);
            // prerequisites = [[1,0],[0,1]]     [current, pre]
            // matrix[pre]: current1, current2, current3

        
        vector<int> d(numCourses, 0); // in-degree, current all degree = 0 
        for(int i = 0; i < numCourses; ++ i)
            for(auto it = matrix[i].begin(); it != matrix[i].end(); ++ it)
                // ++ d[*it]; // all degree +1
                d[*it] = d[*it] + 1;  // all degree in matrix +1

        
        for(int j = 0, i; j < numCourses; ++j)
        {
            for(i = 0; i < numCourses && d[i] != 0; ++ i); // find a node whose in-degree is 0
            // if found degree = 0, break the loop
            // else i add to end(numCourses)
            
            if(i == numCourses) // if not find (all degree > 1, cycle)
                return false;
            
            d[i] = -1; // degree 0 ok!
            for(auto it = matrix[i].begin(); it != matrix[i].end(); ++ it)
                // -- d[*it];
                d[*it] = d[*it] - 1; // all degree in this matrix -1
                // matrix = this pre course
        }
        
        return true;
    }
};

// @lc code=end

