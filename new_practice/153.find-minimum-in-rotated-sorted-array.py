#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# findMin(self, nums: List[int]) -> int:


# @lc code=start
class Solution:
    def findMin(self, nums):
        min_record = pow(2, 31)
        for ele in nums:
            min_record = min(ele, min_record)

        return min_record







        
# @lc code=end

