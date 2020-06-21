#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# n: int) -> List[str]:
# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        res = []
        self.helper(n, 0, "", res)
        return res


    # miss "(())()" 不同步if
    def helper(self, r, l, path, res):
        print("call", path, r, l)
        if r == 0 and l == 0:
            if path not in res:
                res.append(path)
                return

        if r>=1: # r = 1 can add
            # path = path + "("  # []+[]
            # l = l+1
            # r = r-1 # wrong???? global r 提早被改 導致下方if l 運算判斷r 錯誤
            print(path, r, l)
            self.helper(r-1, l+1, path+"(", res)

        if l>=1: # l = 1 can add
            # path = path + ")"  # []+[]
            # l = l-1 # wrong???? global l 提早被改 導致下方if l 運算判斷r 錯誤
            print(path, r, l) 
            self.helper(r, l-1, path+")" , res)

        




            



        
# @lc code=end

