#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
# twoSum(self, numbers: List[int], target: int) -> List[int]:

# @lc code=start
class Solution:
    def twoSum(self, numbers, target):
        my_dict = {}
        
        for idx, ele in enumerate(numbers):
            if target-ele in my_dict.keys():
                return [my_dict[target-ele], idx+1]
            else:
                my_dict[ele] = idx+1

         
                 
# @lc code=end

