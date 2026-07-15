# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # cur go to end of list, track start from tail side backward
        # as recursive return
        # root stay at original head and track from head side forward
        def recur(root: ListNode, cur: ListNode) -> ListNode:
            if not cur:  # reach past end, base case
                return root

            # recursive down to tail
            root = recur(root, cur.next)

            if not root:  # no more root nodes left to pair up, stop
                return None

            tmp = None
            # root and cur met or crossed, means we're at middle, stop linking
            if root == cur or root.next == cur:
                cur.next = None
            else:
                # insert cur right after root (weaving step)
                tmp = root.next
                root.next = cur
                cur.next = tmp

            return tmp

        head = recur(head, head.next)