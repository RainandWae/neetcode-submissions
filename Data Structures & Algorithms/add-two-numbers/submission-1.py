class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node, makes building result easier (no special-case for first node)
        dummy = ListNode()
        # pointer that walks forward building result list
        cur = dummy

        # math, tracks overflow (e.g. 9+9=18, carry 1 to next digit)
        carry = 0

        # keep going while either list has digits left,
        # OR theres a leftover carry
        while l1 or l2 or carry:
            # set digit only if l1 not null, if null then set to 0
            # (handles lists of different lengths, shorter one just contributes 0)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # calculate new digit
            val = v1 + v2 + carry
            carry = val // 10   # overflow goes to next digit (0 or 1)
            val = val % 10      # actual digit to store (0-9)
            cur.next = ListNode(val)

            cur = cur.next               # move result pointer forward
            l1 = l1.next if l1 else None  # move l1 forward if it exists
            l2 = l2.next if l2 else None  # move l2 forward if it exists

        return dummy.next  # skip dummy, return actual head of result