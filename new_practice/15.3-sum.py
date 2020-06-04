#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        
        # # my_dict = {}
        # l = len(nums)
        # nums = sorted(nums)
        # ans_list = []

        # for i in range(l-2):
        #     for j in range(i+1, l-1):
        #         # print(i, j)
        #         # print(nums[i], nums[j])
        #         # print(- (nums[i] + nums[j]))
          

        #         if -(nums[i] + nums[j]) in nums[j+1:l]:
        #             ans = [nums[i], nums[j], -(nums[i] + nums[j])]

        #             if ans not in ans_list:
        #                 ans_list.append(ans)
                    
        # return ans_list

        # TLE 311/313

        # https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)

        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2): #[8]
            if nums[i]>0: break #[7] can not less than 0
            if i>0 and nums[i]==nums[i-1]: continue #[1] repeated i

            l, r = i+1, length-1 #[2] last idx = length-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total<0: #[3] too small left++
                    l+=1
                elif total>0: #[4] too big right--
                    r-=1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]: #[6] repeated l
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6] repeated r
                        r-=1
                    l+=1
                    r-=1
        return res


            

        # my_dict[idx] = 
        # 









# @lc code=end

