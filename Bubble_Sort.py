# [演算法] 氣泡排序法(Bubble Sort)
# 將資料分成
# 已排序：位置 < data.length - i - 1
# 未排序：位置 ≥ data.length - i - 1
# 氣泡排序作法：
# 由未排序中的第一筆開始，與第二筆資料比對
# 若第一筆 > 第二筆 ⇒ 交換位置(Swap)
# 若還有未排序的資料，則用第二筆和第三筆資料比對
# 依此類推
# 若未排序的資料中，比對時都沒有進行交換位置 ⇒ flag = false
# 代表資料已排序好 ⇒ 提早結束排序
# 執行時，未排序資料中的最大值會如同氣泡般往右跑

# 時間複雜度(Time Complexity)
# Best Case：Ο(n)
# 當資料的順序恰好為由小到大時
# 第一次執行後，未進行任何swap ⇒ 提前結束
# Worst Case：Ο(n2)
# 當資料的順序恰好為由大到小時
# 每回合分別執行：n-1、n-2、...、1次
# (n-1) + (n-2) + ... + 1 = n(n-1)/2 ⇒ Ο(n2)
# Average Case：Ο(n2)
# 第n筆資料，平均比較(n-1)/2次

# 空間複雜度(Space Complexity)：θ(1)
# 穩定性(Stable/Unstable)：穩定(Stable)

# [Python] 如何做swap()
# http://ajing-notebook.blogspot.com/2019/02/python-swap.html
# [Python] swap
# http://falldog7.blogspot.com/2009/07/python-swap.html
# # Mar 01 Wed 2017
# 【教學】call by value, call by address, call by reference 差別在哪?
# https://wayne265265.pixnet.net/blog/post/112556555-%E3%80%90%E6%95%99%E5%AD%B8%E3%80%91call-by-value%2C-call-by-address%2C-call-by-referenc

nums = [42,66,52,72,63,89,4,50,15,28]
nums_len = len(nums)

# def swap(a,  b):
#     temp = b
#     b = a
#     a = temp

# def swap2(a,  b):
#     return b , a


# a = 1
# b = 2
# print(1, 2)
# print(swap(1, 2))
# print(a, b)
# swap(a, b)
# print(a, b)
# a , b = swap2(a, b)
# print(a, b)


for i in range(nums_len-1): # start point
    flag = True
    for j in range(nums_len-1-i):  # first finish == maximum in last place
        if nums[j] > nums[j+1]: # 左大右小就要交換
            flag = False
            nums[j], nums[j+1] = nums[j+1], nums[j] # swap

    if flag == True: ## no swap, early stop
        break


print(nums)

