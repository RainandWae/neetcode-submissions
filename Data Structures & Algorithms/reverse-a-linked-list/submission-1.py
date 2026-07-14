# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# linked list recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # default if no next this is new head(last node in original)
        tempHead = head

        if head.next:
            # recurse first, go all the way to
            # the end before doing anything
            # tempHead ends up being the last node, new head of reversed list
            tempHead = self.reverseList(head.next)

            # head.next is the next node, 
            # already reversed by recursion below
            # make that next node point back to current head, flips the arrow
            head.next.next = head
        
        # clear old forward pointer, avoid cycle/dup link
        # gets overwritten again for nodes below, 
        # stays None only for original head = new tail
        head.next = None

        # same tempHead passed up unchanged through every level
        return tempHead