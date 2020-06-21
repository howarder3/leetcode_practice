#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
#  str) -> int:
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s):
        word_dict = {}
        max_len = 0
        cur_len = 0
        ## DP: record word last position
        ## two case
        ## not in dict cur+1
        ## in dict min(cur+1 or -dict pos +1)


        for i in range(len(s)):
            if s[i] in word_dict.keys(): 
                cur_len = min(cur_len+1, i-word_dict[s[i]]) ## e,w,w,e  1,2,1(idx 3- dict 2),2 
                word_dict[s[i]] = i  ## update index
            else: ## not in dict
                word_dict[s[i]] = i  ## record index
                cur_len = cur_len + 1
            
            max_len = max(max_len, cur_len) ## update max_len 
            # if cur_len > max_len:
            #     max_len = cur_len ## update max_len   

        return max_len
        





# @lc code=end

