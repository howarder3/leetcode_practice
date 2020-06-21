#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sumNumbers(self, root: TreeNode) -> int:
    def sumNumbers(self, root):
        if not root:
            return 0

        ans = []
        self.dfs(root, 0, ans)
        # print(ans)

        return sum(ans)


    # def dfs(self, root, num, ans):
    #     # print(root)

    #     if not root:
    #         return

    #     if (root.left is None) and (root.right is None): # leaf, end of num
    #         final_path = path + [root.val]
    #         final_num = "".join(map(str, final_path))
    #         # print(final_num)
    #         # print(final_path[::-1])
    #         # final_path = final_path[::-1]
    #         # final_path = int(float(str(final_path)))
    #         ans.append(int(final_num))


    #     self.dfs(root.left, path+[root.val], ans)
    #     self.dfs(root.right, path+[root.val], ans)

# https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/41383/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively).
    

    def dfs(self, root, num, ans):
        # print(root)

        if not root:
            return

        if (root.left is None) and (root.right is None): # leaf, end of num
            final_num = num*10+root.val
            ans.append(int(final_num))


        self.dfs(root.left, num*10+root.val, ans) # 數值處理
        self.dfs(root.right, num*10+root.val, ans)

# @lc code=end

