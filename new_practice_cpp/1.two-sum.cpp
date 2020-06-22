/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int,int> dict;
        map<int,int>::iterator iter;
        vector<int> ans;

        for (int i=0; i<nums.size();i++){
            
            iter = dict.find(target-nums[i]);
            // cout<<iter;
            // printf("(%d,%d)",iter->first,iter->second);
            if (iter != dict.end()){ // num found
                ans.push_back(iter->second); //nums find in dict (smaller)
                ans.push_back(i); // current index (bigger)                
                return ans;     
            }
            else{ //iter == dict.end(), not found
                dict[nums[i]]=i;    
            }
        }
        return ans;
    }
};
// @lc code=end

