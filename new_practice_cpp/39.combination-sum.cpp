/*
 * @lc app=leetcode id=39 lang=cpp
 *
 * [39] Combination Sum
 */

// @lc code=start
class Solution {
// https://leetcode.com/problems/combination-sum/discuss/16496/Accepted-16ms-c%2B%2B-solution-use-backtracking-easy-understand.
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> path;
        sort(candidates.begin(), candidates.end());

        dfs(candidates, target, ans, path, 0);

        return ans;   
    }

    void dfs(vector<int> &candidates, int target, vector<vector<int>> &ans, 
             vector<int> &path, int begin){
        if(target == 0){ // target == 0
            ans.push_back(path);
            return;
        }

        for (int i=begin; i < candidates.size() && target >= candidates[i]; ++i){
            path.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], ans, path, i);
            path.pop_back();
        }
    }
};


// @lc code=end

