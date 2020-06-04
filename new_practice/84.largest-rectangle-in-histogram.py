#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
# def largestRectangleArea(self, heights: List[int]) -> int:

# @lc code=start
class Solution:
    # def largestRectangleArea(self, heights):
    #     r = 0
    #     l = len(heights)
    #     width = len(heights)

    #     # 右邊比較高, 就是左邊的值繼續用 2,3 => 2,2
    #     # 右邊比較矮, 就是用右邊的值  2,1 => 2,1

    #     r_list = []

    #     # 左邊看過去的感覺
    #     for idx in range(width):
    #         r_list.append(min(heights[i], r_list[-1]))

    #     # 右邊看回來的感覺
    #     for idx in reversed(range(width)):
    #         r_list.append(min(heights[i], r_list[-1]))

    # https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
    def largestRectangleArea(self, height):
        height.append(0) # 最後補上一個0, 把前面結算
        stack = [-1] #LIFO
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]: # 之前的位置比較高(比現在)，要透過乘寬達到更大的長方形
                h = height[stack.pop()] # 取得高度
                w = i - stack[-1] - 1 # stack[-1] = 現在-保存寬度(-1當前)   取得寬
                ans = max(ans, h * w) # 比較目前最大
            stack.append(i) # 每個都存位置
        # height.pop()
        return ans


# stack = -1, 0, 1

# i = 1
# (2>1，如果想透過1得到勝利，必須靠乘寬)
# h = height[0] = 2
# stack[-1] = -1
# w = 1 - (-1) -1 = 1

# 算出 = 2*1


# i = 4
# stack = -1, 1, 2 ,3

# (6>2，如果想透過2得到勝利，必須靠乘寬)
# h = height[3] = 6
# stack[-1] = 2
# w = 4 - 2 -1 = 1

# 算出 = 6*1

# (5>2，如果想透過2得到勝利，必須靠乘寬)
# h = height[2] = 5
# stack[-1] = 1
# w = 4 - 1 -1 = 2


# i = 6
# stack = -1, 1, 4, 5

# (3>0，如果想透過2得到勝利，必須靠乘寬)
# h = height[5] = 3
# stack[-1] = 4
# w = 6 - 4 - 1 = 1

# 算出 = 3*1


# stack = -1, 1, 4
# (2>0，如果想透過2得到勝利，必須靠乘寬)
# h = height[4] = 2
# stack[-1] = 1
# w = 6 - 1 - 1 = 4

# 算出 = 2*4
        

# stack = -1, 1
# (1>0，如果想透過2得到勝利，必須靠乘寬)
# h = height[1] = 1
# stack[-1] = -1
# w = 6 - (-1) - 1 = 6

# 算出 = 1*6

# stack = -1
# (-1>0)




# @lc code=end

