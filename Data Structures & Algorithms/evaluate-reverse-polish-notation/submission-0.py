class DoublyLinkedList:
    def __init__(self, val, next=None, prev=None):
        #value store in current node
        self.val = val
        # pointer to next
        self.next = next
        # pointer to prev
        self.prev = prev

#usage of double linked list
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create first node, using first token
        head = DoublyLinkedList(tokens[0])
        # set as current
        curr = head

        # convert token array to doubly linked list 
        for i in range(1, len(tokens)):
            # create next node, link previous node to current
            curr.next = DoublyLinkedList(tokens[i], prev=curr)
            # move current pointer forward
            curr = curr.next
        
        # start scanning linked list from beginning
        while head is not None:
            # hit an operator 
            if head.val in "+-*/":
                # go back 2 time store as l
                l = int(head.prev.prev.val)
                # go back 1 store as r
                r = int(head.prev.val)

                # math operation
                if head.val == '+':
                    temp = l + r
                elif head.val == '-':
                    temp = l - r
                elif head.val == '*':
                    temp = l * r
                else:
                    temp = int(l / r)

                # replace token operator(+-*/) with answer
                head.val = str(temp)

                # token operator got replaced with new value
                # current l+r not needed
                # 3*prev => go back 3 time, replace that value with
                # current prev(back 1 time of head)
                # head.prev.prev is skipped ==> basically deleted
                # head.prev got replaced
                head.prev = head.prev.prev.prev

                # reconnect linked list
                if head.prev is not None:
                    # make previous node point to current head
                    head.prev.next = head

            # latest value seen after calculation
            ans = int(head.val)
            # iterate to next node
            head = head.next

        return ans