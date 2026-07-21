# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # empty = same
        if not p and not q:
            return True

        # one of them empty but not other
        # or value is not equal each other
        if not p or not q or p.val != q.val:
            return False

        # call recursive, on left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return the value if true or not