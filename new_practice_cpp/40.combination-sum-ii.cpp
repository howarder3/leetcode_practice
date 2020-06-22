/*
 * @lc app=leetcode id=40 lang=cpp
 *
 * [40] Combination Sum II
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {

        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ans;
        vector<int> path;

        dfs(candidates, target, ans, path, 0);

        return ans;        
    }

    void dfs(vector<int> &candidates, int target, vector<vector<int>> &ans,
             vector<int> &path, int begin){
        
        if(target == 0 && find(ans.begin(), ans.end(), path) == ans.end()){ // ans.end() means not found
            ans.push_back(path);
            return;
        }

        for(int i=begin; i<candidates.size() && target >= candidates[i] ;i++){
            path.push_back(candidates[i]);
            dfs(candidates, target-candidates[i], ans, path, i+1); // i+1 means next
            path.pop_back();
        }
    }
};
// @lc code=end

