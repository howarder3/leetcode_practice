#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s):
        final_ans = "" 
        for i in range(len(s)):
            # odd case
            r = i
            l = i
            while(r < len(s) and l >= 0):
                if s[l] == s[r]: 
                    temp_ans = s[l:r+1]
                    # print(temp_ans)
                    if len(temp_ans) > len(final_ans):
                        final_ans = temp_ans
                    l = l - 1
                    r = r + 1
                else:
                    break
            # # odd case
            # l = i
            # r = i - 1


            ## even case
            r = i
            l = i-1
            while(r < len(s) and l >= 0):
                if s[l] == s[r]: 
                    temp_ans = s[l:r+1]
                    # print(temp_ans)
                    if len(temp_ans) > len(final_ans):
                        final_ans = temp_ans
                    l = l - 1
                    r = r + 1
                else:
                    break




        return final_ans





# @lc code=end

