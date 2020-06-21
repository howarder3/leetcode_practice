#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start

class Solution:
    def canJump(self, nums):
        
        if len(nums) == 1: return True

        # max_position = [i for i in range(len(nums))]
        # max_position = [0]*len(nums)

        max_position = [idx+ele for idx, ele in enumerate(nums)]
        print((max_position))
        print(len(max_position))

        current_max = max_position[0]
        for i in range(len(nums)):
            if i > current_max: # not found
                return False
            if max_position[i] > current_max: # update max
                current_max = max_position[i]


        return True





# @lc code=end

