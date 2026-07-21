# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if sub tree is empty, empty can be inside org tree
        if not subRoot:
            return True

        # if org tree is empty, sub cannot be in empty tree
        if not root:
            return False

        # if same same
        if self.sameTree(root, subRoot):
            return True

        # check subtree of org tree, left to right, compare to subroot
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))


    # helper function
    def sameTree(self, root, subRoot):
        # both empty, return true
        if not root and not subRoot:
            return True
        
        # non empty, compare tree 
        if root and subRoot and root.val == subRoot.val: 
            return (self.sameTree(root.left, subRoot.left) and
            self.sameTree(root.right, subRoot.right))

        return False