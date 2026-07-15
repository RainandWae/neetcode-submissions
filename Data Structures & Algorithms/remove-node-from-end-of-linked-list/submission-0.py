# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recur(self, head, n):
        if not head:  # base case, reached past end
            return None

        # recur all the way to tail
        head.next = self.recur(head.next, n)

        # on the way back up, count down n for each node passed
        n[0] -= 1

        # n hits 0 = this is the node to remove, skip it
        if n[0] == 0:
            return head.next

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # wrap n in a list so it's mutable across recursive calls 
        # (passed by reference)
        return self.recur(head, [n])