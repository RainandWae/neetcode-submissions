class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])  # BFS, level by level
        while queue:
            node = queue.popleft()

            # swap left and right children
            node.left, node.right = node.right, node.left

            # add children to queue to process next
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root