#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# : str   -> List[str]
# @lc code=start

class Solution:
    def letterCombinations(self, digits):    

        if not digits:
            return []
        
        ans_list = [""]
        phone_dict = {
            '2':'abc', '3':'def', '4':'ghi',
            '5':'jkl', '6':'mno', '7':'pqrs',
            '8':'tuv', '9':'wxyz'
        } 

        # print([ele for ele in phone_dict['2']])  #a, b, c
        for i in range(len(digits)):

            
            # print(
            #     ['a' + ele2 
            #     for ele2 in phone_dict[digits[i]]]
            # )

            ans_list =  [
                ele1 + ele2 
                for ele1 in ans_list 
                for ele2 in phone_dict[digits[i]]
            ]  #a, b, c

        return ans_list


        # for i in range(len(digits)):
            # print(for ele in phone_dict[digits[i]])  #a, b, c

            # digits[i] 



        
# Python solution
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution
# list add list (接在後面)


# @lc code=end

