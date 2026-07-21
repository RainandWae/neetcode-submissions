# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # create function to return Bool and height
        def dfs(root):
            # base case
            if not root:
                return [True, 0]

            # try to determine, starting from left
            # is subtree balance, recursive all to leaf
            left = dfs(root.left)
            right = dfs(root.right)

            # left and right bool value are true
            # and absolute value of height left right <= 1 then balanced
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            # return pair value, is the tree balanced for entire tree
            # and return height of tree 
            # calculate height by adding 1(current root currently at)
            # plus highest value of height left and right 
            return [balanced, 1 + max(left[1], right[1])]

        # call our function start root note, return index 0(bool value)
        return dfs(root)[0]