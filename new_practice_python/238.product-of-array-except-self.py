#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# nums: List[int]) -> List[int]:
# @lc code=start
class Solution:
    def productExceptSelf(self, nums):
        # if 0 in nums:
        #     return nums

        # product = 1
        # out = []
        # for ele in nums:
        #     product = product * ele

        # for ele in nums:
        #     out.append(int(product/ele))

        # return out

    # @param {integer[]} nums
    # @return {integer[]}
    # Python solution (Accepted), O(n) time, O(1) space
    # https://leetcode.com/problems/product-of-array-except-self/discuss/65625/Python-solution-(Accepted)-O(n)-time-O(1)-space
    # def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output



        
        
# @lc code=end

