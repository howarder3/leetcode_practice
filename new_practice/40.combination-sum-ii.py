#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
    def combinationSum2(self, candidates, target): 
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
            if path not in res:
                res.append(path)
                return

        for idx in range(len(candidates)):
            ele = candidates[idx]
            # print(ele)
            self.helper(candidates[idx+1:], target-ele, path+[ele], res) 
            # candidates[idx+1:] 往後搜尋
            # path+[ele] 只有這次的ele, 改為list加入path








# @lc code=end

