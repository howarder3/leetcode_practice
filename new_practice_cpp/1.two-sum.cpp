/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        vector<int> ans;
        map<int, int> HashTable;
        map<int, int>::iterator iter;

        for(int i=0; i<nums.size(); i++){
            iter = HashTable.find(target - nums[i]);

            // for (map<int, int>::iterator it=HashTable.begin(); it != HashTable.end(); it++)
            // {
            //     printf("(%d,%d)\n",iter->first, iter->second);
            // }

            if(iter != HashTable.end()){
                // cout << iter->first << iter->second << endl;
                // printf("(%d,%d)\n",iter->first, iter->second);
                ans.push_back(iter->second);
                ans.push_back(i);
                return ans;
            }
            else{
                HashTable.insert(pair<int,int>(nums[i],i));
            }
        }
        return ans;
    }
};
// @lc code=end

