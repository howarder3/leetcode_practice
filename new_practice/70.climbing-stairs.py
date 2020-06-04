#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
# climbStairs(self, n: int) -> int:

# @lc code=start
class Solution:
    def climbStairs(self, n):
        record_list = [0]

        for i in range(1, n+1):
            if i == 1:
                record_list.append(1)
            elif i == 2:
                record_list.append(2)
            else:
                record_list.append(record_list[i-1] + record_list[i-2])


        return record_list[n]




            
            




        
# @lc code=end

