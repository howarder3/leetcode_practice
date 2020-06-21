#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum

#  nums : List[int]
#  target: int

# List[int]

# @lc code=start


class Solution:
    def twoSum(self, nums, target): # 2 7 11 15
        # for idx, ele in enumerate(nums):
        #     # print(idx, ele) # 0 2
        #     if target - ele in nums[idx+1:]:
        #         if target - ele == ele:
        #             return [nums.index(ele), (nums[idx+1:].index(target - ele))+idx+1]
        #         else:
        #             return [nums.index(ele), nums.index(target - ele)]


        #     else:
        #         pass

        my_dict = {}
        for idx, ele in enumerate(nums):
            rest = target - ele
            if rest in my_dict:
                return [my_dict[rest], idx]
            else:
                my_dict[ele] = idx # record




       
# @lc code=end

