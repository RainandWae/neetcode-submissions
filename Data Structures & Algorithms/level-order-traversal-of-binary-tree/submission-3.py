# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS layer by layer
# Queue, fifo
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            layer = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    layer.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if layer:
                result.append(layer)

        return result