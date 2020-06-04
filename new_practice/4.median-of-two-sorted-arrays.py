#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# nums1: List[int], 
# nums2: List[int]) 
# float:

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 , n2 = len(nums1) , len(nums2)  
        if (n1 + n2)%2 == 1 : # odd case
            find_num = (n1 + n2) / 2 + 0.5# (2+1)/2=1.5 need+0.5 => find 2
            for i in range(int(find_num)):
                if not nums1: # nothing have find s2
                    current_num = nums2[0]
                    nums2.remove(current_num)
                elif not nums2:    
                    current_num = nums1[0]
                    nums1.remove(current_num)

                elif  nums1[0] <= nums2[0]:
                    current_num = nums1[0]
                    nums1.remove(current_num)
                else:
                    current_num = nums2[0]
                    nums2.remove(current_num)         
            return current_num



        else: # even case
            find_num = (n1 + n2) / 2 # (2+2)/2=2  => find 2, 3(current_num)
            current_num = 0

            for i in range(int(find_num+1)):
                num_before = current_num
                if not nums1: # nothing have find s2
                    current_num = nums2[0]
                    nums2.remove(current_num)
                elif not nums2:    
                    current_num = nums1[0]
                    nums1.remove(current_num)

                elif nums1[0] <= nums2[0]:
                    current_num = nums1[0]
                    nums1.remove(current_num)
                else:
                    current_num = nums2[0]
                    nums2.remove(current_num)    

            

            return (num_before + current_num) / 2
            


        
# @lc code=end

