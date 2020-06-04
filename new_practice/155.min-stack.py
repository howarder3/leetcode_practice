#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    # https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [[-1, pow(2, 31)]]
        

    def push(self, x):
        self.stack.append([x, min(self.stack[-1][1], x)])

    def pop(self):
        if len(self.stack) > 1:
            self.stack.pop() 

    def top(self):
        if len(self.stack) == 1:
            return null
        if len(self.stack) > 1:
            return self.stack[-1][0]  

      
    def getMin(self):
        if len(self.stack) == 1:
            return null
        if len(self.stack) > 1:
            return self.stack[-1][1]  

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

