#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    # def romanToInt(self, s: str) -> int:
    def romanToInt(self, s):
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        roman_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        roman_dict2 = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        if len(s) == 0:
            return 0
        
        mysum = 0
        idx = 0
        while(idx<len(s)):
            if idx+1 < len(s) and s[idx]+s[idx+1] in roman_dict2:
                mysum = mysum + roman_dict2[s[idx]+s[idx+1]] 
                idx = idx + 2
            else:
                mysum = mysum + roman_dict[s[idx]]
                idx = idx + 1

        return mysum
        
# @lc code=end

