/*
 * @lc app=leetcode id=14 lang=cpp
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
public:
    // string longestCommonPrefix(vector<string>& strs) {
    //     string ans = "";
    //     string target = strs[0];
    //     for(int i=0; i<target.length(); i++){
    //         for(int j=1; j<strs.size(); j++){
    //             if(strs[j].find(target[i]) != strs[j].end())
    //                 return ans;
    //         }
    //         ans += target[i];
    //     }
    // }
    // https://leetcode.com/problems/longest-common-prefix/discuss/6926/Accepted-c%2B%2B-6-lines-4ms
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        for(int str_idx=0; strs.size()>0; str_idx++){
            for(int i=0; i<strs.size(); i++) {// search all strs
                if(str_idx >= strs[i].size()){
                    return prefix;
                } //oversize
                if(i > 0 && strs[i][str_idx] != strs[i-1][str_idx]){
                    return prefix;
                }
            }
            prefix += strs[0][str_idx];
        }
        return prefix;
    }
};




// @lc code=end

