#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# : List[int]  -> None:
# @lc code=start
class Solution:

    # TLE: 13/265 cases passed (N/A)

    # def nextPermutation(self, nums):
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     if len(nums) == 1:
    #         return nums

    #     res = []
    #     self.dfs(sorted(nums), [], res)

    #     print(res)
    #     idx = res.index(nums)
    #     # print(idx)
    #     # print(res[1])
    #     # print(res[idx+1])

    #     # modify nums in-place instead.
    #     i = 0
    #     while(i<len(nums)):
    #         nums[i] = res[(idx+1)%len(res)][i]
    #         i = i + 1

        


        
    # def dfs(self, nums, path, res):
    #     if not nums:
    #         if path not in res:
    #             res.append(path)
    #             return 

    #     for idx, ele in enumerate(nums):
    #         # print(nums)
    #         self.dfs(nums[:idx]+nums[idx+1:], path+[ele], res)


    # def nextPermutation(self, nums):
    #     i = j = len(nums)-1 #最後一個數字
    #     while i > 0 and nums[i-1] >= nums[i]:
    #         i -= 1
    #     if i == 0:   # nums are in descending order
    #         nums.reverse()
    #         return 
    #     k = i - 1    # find the last "ascending" position
    #     while nums[j] <= nums[k]:
    #         j -= 1
    #     nums[k], nums[j] = nums[j], nums[k]  
    #     l, r = k+1, len(nums)-1  # reverse the second part
    #     while l < r:
    #         nums[l], nums[r] = nums[r], nums[l]
    #         l +=1 ; r -= 1


    def nextPermutation(self, nums):
        for i in range(len(nums)-1, -1, -1):
            if i-1 >=0 and nums[i] > nums[i-1]:
                for j in reversed(range(i,len(nums))):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                nums[i:] = nums[i:][::-1]
                break
        else:
            nums = nums.reverse()


        
# @lc code=end

