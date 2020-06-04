# 插入排序作法：
# 將資料分成已排序、未排序兩部份
# 依序由未排序中的第一筆(正處理的值)，插入到已排序中的適當位置
# 插入時由右而左比較，直到"遇到第一個比正處理的值小的值"，再插入
# 比較時，若遇到的值比正處理的值大或相等，則將值往右移

# 時間複雜度(Time Complexity)
# Best Case：Ο(1)
# 當資料的順序恰好為由小到大時，每回合只需比較1次
# Worst Case：Ο(n2)
# 當資料的順序恰好為由大到小時，第i回合需比i次
# Average Case：Ο(n2)
# 第n筆資料，平均比較n/2次

# 空間複雜度(Space Complexity)：θ(1)
# 穩定性(Stable/Unstable)：穩定(Stable)

nums = [42,66,52,72,63,89,4,50,15,28]
nums_len = len(nums)

for i in range(1, nums_len): # 第一個不比, 右大左小才正常
    target = nums[i]
    print("target: ", target)
    if nums[i-1] < nums[i]:
        pass
    else: # now,與自己左邊開始比  右邊比較小, 往回插入, 放比他大的右邊
        for j in range(i, -1, -1):  # i ~ 0
            # print(j) # 自己現在的位置
            if target < nums[j-1] and j >= 1:  # 與自己左位置比較 target依然小 左邊(比較大的數字)往右複製 # j=0 最小了
                nums[j] = nums[j-1] # start nums[i] = nums[i-1]
            else: # temp比較大 可插入
                nums[j] = target
                break # 已插入, 停止比較
            
            # print(nums)



print(nums)

