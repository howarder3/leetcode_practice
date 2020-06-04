#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start

# List[List[int]]

class Solution:
    # def merge(self, intervals):
    #     ans_list = []
    #     intervals.sort(key=lambda s:s[0])


    #     idx = 0
    #     while(idx < len(intervals)): # 0 ~ end-1
    #     # for idx in range(len(intervals)): # 0 ~ end-1
    #         print("test", idx)
    #         r = intervals[idx][0]
    #         l = intervals[idx][1]
    #         # l = intervals[idx][1]
    #         # r = intervals[idx+1][0]

    #         while(idx < len(intervals)-1 and intervals[idx][1] >= intervals[idx+1][0]):
    #             # print(idx)

    #             if intervals[idx+1][1] < intervals[idx][1]: # new left still less than original left
    #                 pass
    #             else:
    #                 l = intervals[idx+1][1] # intervals change next left
    #             idx = idx + 1 
    #             print(idx)
                    
    #         ans_list.append([r, l])
    #         idx = idx + 1 

    #     return ans_list


    def merge(self, intervals):
        
        if len(intervals) <= 1:
            return intervals

        ans_list = []
        # intervals.sort(key=lambda s: s.start)
        intervals = sorted(intervals, key=lambda s: s[0])
        # intervals = sorted(intervals, key = lambda x: x.start)
        # for i in sorted(intervals, key=lambda i: i.start):

        ans_list.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans_list[-1][1]:
                ans_list[-1][1] = max(intervals[i][1], ans_list[-1][1])

            else:
                ans_list.append(intervals[i])

        return ans_list






# @lc code=end

