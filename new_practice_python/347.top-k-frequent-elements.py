#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
#  List[int], k: int) -> List[int]:
# @lc code=start
class Solution:
    def topKFrequent(self, nums, k):
        my_dict = {}
        for ele in nums:
            if ele not in my_dict:
                my_dict[ele] = 0
            else:
                my_dict[ele] = my_dict[ele] + 1


        sorted_dict = sorted(my_dict.items(), key = lambda x: x[1], reverse=True)
        print(sorted_dict) # [(1, 2), (2, 1), (3, 0)]
        ans_list = []
        for i in range(k):
            ans_list.append(sorted_dict[i][0])

        return ans_list








        
# @lc code=end

