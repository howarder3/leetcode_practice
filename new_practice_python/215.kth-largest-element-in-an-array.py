#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# List[int], k: int) -> int:
# @lc code=start
class Solution:
    def findKthLargest(self, nums, k): 

        k_list = nums[:k] # first k # 0 1 2 (K=3)
        # save k and delete min 

        for i in range(k, len(nums)): #3 start (K=3)
            if nums[i] > min(k_list):
                # print(min(k_list))
                k_list.remove(min(k_list))
                k_list.append(nums[i])


        return min(k_list)

        # print(nums)
        # heapq.heapify(nums)
        # print(nums)

        # Python min-heap and quick partition solutions (O(nlogn) and O(n) time complexities).
        # https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60535/Python-min-heap-and-quick-partition-solutions-(O(nlogn)-and-O(n)-time-complexities).
                
        # k+(n-k)*log(k) time

# python heapq library
# https://docs.python.org/zh-tw/3/library/heapq.html

# def findKthLargest1(self, nums, k):
#     heap = nums[:k]
#     heapq.heapify(heap)  # create a min-heap whose size is k 
#     for num in nums[k:]:
#         if num > heap[0]:
#            heapq.heapreplace(heap, num)
#         # or use:
#         # heapq.heappushpop(heap, num)
#     return heap[0]
  
# # O(n) time, quicksort-Partition method   
# def findKthLargest(self, nums, k):
#     pos = self.partition(nums, 0, len(nums)-1)
#     if pos > len(nums) - k:
#         return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
#     elif pos < len(nums) - k:
#         return self.findKthLargest(nums[pos+1:], k)
#     else:
#         return nums[pos]
 
# # Lomuto partition scheme   
# def partition(self, nums, l, r):
#     pivot = nums[r]
#     lo = l 
#     for i in xrange(l, r):
#         if nums[i] < pivot:
#             nums[i], nums[lo] = nums[lo], nums[i]
#             lo += 1
#     nums[lo], nums[r] = nums[r], nums[lo]
#     return lo









# @lc code=end

