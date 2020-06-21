#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# List[List[int]]) -> None:
# @lc code=start
class Solution:
    def rotate(self, matrix): 
        """
        :type matrix: List[List[int]]
        Do not return anything, modify matrix in-place instead.
        """

        # 38 ms, easy to understand, first transpose, then flip horizontally
        # 1 line in Python
        #  https://leetcode.com/problems/rotate-image/discuss/18888/1-line-in-Python
        # matrix[::] = zip(*matrix[::-1])
        # Seven Short Solutions (1 to 7 lines)
        # https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # flip horizontally
        for i in range(n):
            for j in range(int(n/2)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1- j] = tmp


        
# @lc code=end

