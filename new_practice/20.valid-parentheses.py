#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    # def isValid(self, s: str) -> bool:
    def isValid(self, s):

        if len(s) == 0:
            return True
        if len(s) == 1:
            return False

        left = ['(','[','{']
        idx = 0
        stack = []

        while(idx < len(s)):
            if s[idx] in left:
                stack.append(s[idx])
                idx = idx + 1
            else:
                if len(stack) > 0:
                    target = stack.pop()
                else:
                    return False
                    
                if target == '(' and s[idx] == ')':
                    idx = idx + 1
                elif target == '[' and s[idx] == ']':
                    idx = idx + 1
                elif target == '{' and s[idx] == '}':
                    idx = idx + 1
                else:
                    return False

        if len(stack) == 0: # nothing in stack
            return True
        else:
            return False


# "{[]}"
        
# @lc code=end

