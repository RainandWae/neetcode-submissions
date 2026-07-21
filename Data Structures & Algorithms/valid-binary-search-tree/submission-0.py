class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # each node must fall within a valid range (left, right)
        # range gets narrower as we go deeper
        def valid(node, left, right):
            if not node:  # empty subtree, always valid
                return True

            # node val must be strictly between the allowed bounds
            if not (left < node.val < right):
                return False

            # going left: upper bound becomes
            # node.val (everything left must be smaller)
            
            # going right: lower bound becomes
            # node.val (everything right must be bigger)
            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))

        # start with no limits, root can be anything
        return valid(root, float("-inf"), float("inf"))