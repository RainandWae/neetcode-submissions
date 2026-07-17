# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Each call doesn't know its depth
# just ask children how deep are you
# add 1 to whichever one is bigger
# The depth number only gets built as answers bubble back up from the leaves to the root, never on the way down.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root):
            nonlocal result

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            result = max(result, left + right)

            return 1 + max(left, right)

        dfs(root)
        return result