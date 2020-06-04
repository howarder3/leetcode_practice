#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# trap(self, height: List[int]) -> int:

# @lc code=start
class Solution:
    # def trap(self, height):
        # Input: [0,1,0,2,1,0,1,3,2,1,2,1]
        # Output: 6

        # 0,1,0,2,1,0,1,3,2,1,2,1
        #  

        # mylen = len(height)
        # l = 0  
        # r = mylen - 1
        # res = 0
        # while():

    # https://leetcode.com/problems/trapping-rain-water/discuss/17554/Share-my-one-pass-Python-solution-with-explaination
    # def trap(self, bars):
    #     if not bars or len(bars) < 3: # 長度不夠
    #         return 0

    #     volume = 0
    #     left, right = 0, len(bars) - 1
    #     l_max, r_max = bars[left], bars[right] # 水槽高度
    #     while left < right: # 跑到交錯
    #         l_max, r_max = max(bars[left], l_max), max(bars[right], r_max) 
    #         # 除非左邊有更高的就更新, 右邊有更高的就更新

    #         # 右邊水位比較高的, 左邊往右移
    #         if l_max <= r_max:
    #             volume += l_max - bars[left]
    #             left += 1

    #         # 左邊比較高, 右邊往左移
    #         else:
    #             volume += r_max - bars[right]
    #             right -= 1

    #     return volume


# [0,1,2,3,4,5,6,7,8,9,10,11]
# 高度 =  [0,1,0,2,1,0,1,3,2,1,2,1]  #

# 指標
# left =  [0,1,"0",2,"1",0,"1",3, , , , ]  # r變2, l找比2更高的
# right = [ , , , , , , , ,2,1,2,1]

# 水位
# l_max = [0,1,"1",2,"2",2,"2",3, , , , ]
# r_max = [ , ,  ,  ,  ,  ,  ,2,2,2,2,1]


# 現有的水位 (max - current)
# volume = [0, +0(1-1), +1(1-0), +0(2-2), , , , ,+0(2-2), +1(2-1), +0(2-2), +0(1-1)]

        

    # https://leetcode.com/problems/trapping-rain-water/discuss/17528/Easy-to-understand-Python-10-line-60ms-O(n)
    # def trap(self, height):
    #     waterLevel = []
    #     left = 0
    #     for h in height:
    #         left = max(left, h)  #發現更高的 就開始加更高的
    #         waterLevel += [left] # over-fill it to left max height



    #     right = 0
    #     for i, h in reversed(list(enumerate(height))): # 11 - 0
    #         right = max(right, h) # 如果有更高的 就更高的
    #         waterLevel[i] = min(waterLevel[i], right) - h  
            
    #         # min(waterLevel[i], right) 取真實高度跟最高高度中比較矮的 減掉 現在的高度
            
    #         # drain to the right height

    #     return sum(waterLevel)




            








        
# @lc code=end

