#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# List[str]) -> List[List[str]]:
# @lc code=start

# 5-line Python solution, easy to understand
# https://leetcode.com/problems/group-anagrams/discuss/19202/5-line-Python-solution-easy-to-understand

class Solution:
    def groupAnagrams(self, strs):
        mydict = {}
        for w in strs:
            key = tuple(sorted(w))
            print(key)

            # print(mydict.get(key, []))
            # print(mydict.get(key))

            if key not in mydict:
                mydict[key] = [w]
            else:
                mydict[key] = mydict[key] + [w]


            # d[key] = d.get(key, []) + [w]
            # mydict[key] = mydict[key] + [w]
            # print(mydict.get(key, []))
            # print(mydict.get(key))



        return mydict.values()



        
# @lc code=end

