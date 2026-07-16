"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# RECURSION AND HASHMAP
class Solution:
    def __init__(self):
        self.oldToCopy = {}  # map original node -> its copy
        # avoids duplicate copies + handles cycles

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # base case, end of list
        if head is None:
            return None

        # already copied this node before (random pointer looped back to it)
        # return existing copy instead of making a new one
        if head in self.oldToCopy:
            return self.oldToCopy[head]

        # make copy of current node (val only for now)
        copy = Node(head.val)
        # register copy BEFORE recursing, 
        # so if random points back here later, we don't loop forever
        self.oldToCopy[head] = copy

        # recursively copy rest of list
        copy.next = self.copyRandomList(head.next)
        # random might be None or already copied node, either works with .get
        copy.random = self.oldToCopy.get(head.random)

        return copy