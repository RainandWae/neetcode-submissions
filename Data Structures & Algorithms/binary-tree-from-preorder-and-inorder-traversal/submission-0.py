class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case, nothing left to build
        if not preorder or not inorder:
            return None

        # preorder: root always comes first
        root = TreeNode(preorder[0])

        # inorder: everything left of root's position = left subtree
        #          everything right of root's position = right subtree
        mid = inorder.index(preorder[0])

        # left subtree size = mid, so grab that many elements after the root in preorder
        # inorder left side is just inorder[:mid]
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        # rest of preorder (after left subtree) = right subtree
        # inorder right side is inorder[mid+1:]
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root