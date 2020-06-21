#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# List[int], target: int) -> List[List[int]]:
# @lc code=start
class Solution:
    def combinationSum(self, candidates, target): 
        res = []
        path = []
        candidates.sort()
        self.helper(candidates, target, path, res)

        return res




    def helper(self, candidates, target, path, res):
        # print(path)
        if target < 0: # wrong early return
            return

        if target == 0: # correct return 
            if path not in res: # 防止重複答案
                res.append(path)
                return

        for idx in range(len(candidates)):
            ele = candidates[idx]
            # print(ele)
            self.helper(candidates[idx:], target-ele, path+[ele], res) 
            # candidates 全部搜尋
            # candidates[idx:] 往後搜尋(含自己)
            # candidates[idx+1:] 往後搜尋,比自己更大的(不含自己)
            # path+[ele] 只有這次的ele, 改為list加入path







# @lc code=end

