# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # temp node, makes it easy to build result without special-casing head
        temp = ListNode()
        # pointer that walks forward, builds the merged list
        leaf = temp

        while list1 and list2:
            # pick smaller val, attach to result, move that list forward
            if list1.val < list2.val:
                leaf.next = list1
                list1 = list1.next
            else:
                leaf.next = list2
                list2 = list2.next
            leaf = leaf.next  # move leaf forward too

        # one list ran out, attach whatever's left of the other (already sorted)
        leaf.next = list1 or list2

        return temp.next  # skip temp node, return actual head