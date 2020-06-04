#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        # l = len(height)
        # max_area = 0
        # for idx1, h1 in enumerate(height[:-1]):
        #     for idx2, h2 in enumerate(height[idx1+1:]):
        #         area = (min(h2, h1)) * (idx2+1 - idx1)
        #         print(idx1, idx2, min(h1, h2))
        #         print(area)


        # for idx1 in range(l-1):
        #     for idx2 in range(idx1+1, l):
        #         area = (min(height[idx1], height[idx2])) * (idx2 - idx1)
        #         # print(idx1, idx2, min(height[idx1], height[idx2]))
        #         # print(area)

        #         if area >= max_area:
        #             max_area = area

        # return max_area

        # TLE O(n^2)

        # https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
        # O(n)
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]: # j side higher, i need more higher (to get more water)
                i += 1
            else: # i side higher, j need more higher (to get more water)
                j -= 1
        return water



# @lc code=end

