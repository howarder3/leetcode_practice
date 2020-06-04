#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
#  List[int]) -> List[List[int]]:

# @lc code=start
class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

        # ans_list = []

        # if nums:
        #     for i in range(len(nums)):
        #         # print(nums[:i], [nums[i]], nums[i+1:])
        #         ans_list = [ a + [nums[i]] + c 
        #             for a in self.permute(nums[:i]) 
        #             for c in self.permute(nums[i+1:])
        #             ]
        #         print(ans_list)
        # else:
        #     return [[]]


        # return ans_list

        ## dfs
    def dfs(self, nums, path, res):
        if nums:
            for i in range(len(nums)): # list add list
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
                print(path, nums[i]) # list add list
        else: ## no nums 
            res.append(path)
            # return # backtracking

# Simple Python solution (DFS).
# https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
# [Python3] backtracking
# https://leetcode.com/problems/permutations/discuss/360280/Python3-backtracking

        

        
# @lc code=end

