#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# List[int]) -> List[List[int]]:

# @lc code=start

# Python easy to understand solutions (DFS recursively, Bit Manipulation, Iteratively).
# https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).

class Solution: 
    # miss (1, 3)
    def subsets(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if path not in res:
            res.append(path)
            # print(res)

        if not nums:
            return

        for i in range(len(nums)): # need sort in order
            # print(nums[i])
            # print(nums[i+1:])
            self.dfs(nums[i+1:], path+[nums[i]] , res)

    # if [1,2,3] == [2,1,3]: # different position
    #     print("True")
    # mylist = []
    # mylist.append(2)
    # mylist.append(1)
    # print(mylist)


    # DFS recursively 
    # def subsets(self, nums):
    #     res = []
    #     self.dfs(sorted(nums), 0, [], res)
    #     return res
        
    # def dfs(self, nums, index, path, res):
    #     res.append(path)
    #     for i in range(index, len(nums)):
    #         self.dfs(nums, i+1, path+[nums[i]], res)


        

    # def helper(self, nums, res):
    #     if nums not in res:
    #         res.append(nums)
    #         print(nums)

    #     if not nums:
    #         return

    #     for i in range(len(nums)): 

    #         print(nums[:i], nums[i] , nums[i+1:])
    #         self.helper(nums[:i], res)
    #         # print(nums[:i])

    #         # print(nums[i:])
    #         self.helper(nums[i+1:], res)
    #         # print(nums[i:])


# @lc code=end

