#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# divide(self, dividend: int, divisor: int) -> int:

# @lc code=start
class Solution:
    # def divide(self, dividend, divisor):
        
    #     if dividend >= pow(2,31):
    #         dividend = pow(2,31) - 1

    #     if dividend < -pow(2,31):
    #         dividend = -pow(2,31) + 1
    #     # 2147483648

    #     if divisor <= 0:
    #         mod = dividend%divisor
    #         print(mod)
    #         if mod == 0:
    #             res = (dividend-mod)/divisor
    #         else:
    #             res = (dividend-mod)/divisor + 1
            
    #     else:
    #         mod = dividend%divisor
    #         res = (dividend-mod)/divisor



    #     if res >= pow(2,31):
    #         res = pow(2,31) - 1

    #     return int(res)

    # https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code
    # def divide(self, dividend, divisor):
    #     positive = (dividend < 0) is (divisor < 0) # 正正得正, 負負得正
    #     dividend, divisor = abs(dividend), abs(divisor) # 都轉成正的
    #     res = 0

    #     while dividend >= divisor: 
    #         temp, i = divisor, 1
    #         # 第二輪處理剩下的 (dividend >= divisor) 的case
    #         while dividend >= temp:  # 還比較大
    #             dividend -= temp # 減一次temp 減到極限
    #             res += i
    #             # <<= 1, 乘2
    #             i <<= 1
    #             temp <<= 1

    #         # print("dividend:", dividend)
    #         # print("res:", res)
    #         # print("temp:", temp)
    #         # print("i:", i)
            

    #         if not positive: # 如果是負的話
    #             res = -res

    #         return min(max(-2147483648, res), 2147483647)
    #         # max(-2147483648, res) # 比最小值還小的話就是最小值(-2147483648)
    #         # min(, 2147483647) # 比最大值還大的話就是最大值(2147483647)

    def divide(self, dividend, divisor):     
        neg=( (dividend < 0) != (divisor < 0) ) # 正正得正, 負負得正
        dividend = left = abs(dividend) # 取正後除
        divisor  = div  = abs(divisor) # 取正後除
        Q = 1
        ans = 0
        while left >= divisor: # 剩餘要除的還比 divisor大 -> 繼續除
            left -= div # 減掉一次 div
            ans  += Q  # 答案+Q
            Q    += Q  # Q 2倍 (商)
            div  += div # div 2倍 (被除數)
            if left < div: # div變得比 剩餘要除的 大了 
                div = divisor # 還原 divisor
                Q = 1 # 還原 Q

        if neg: #如果負的 比最小值還小的話就是最小值(-2147483648)
            return max(-ans, -2147483648)
        else: #如果正的 比最大值還大的話就是最大值(2147483647)
            return min(ans, 2147483647)




# @lc code=end

