class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat array as linked list: 
        # index -> nums[index] is the "next" pointer
        # duplicate number means 
        # two indices point to same place -> creates a cycle
        # Floyd's cycle detection(same as linked list cycle problem)

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]          # move 1 step
            fast = nums[nums[fast]]    # move 2 steps
            if slow == fast:           # they meet -> cycle found
                break

        # phase 2: find entrance of the cycle (= the duplicate number)
        # reset one pointer to start, move both 1 step at a time
        # where they meet again = start of cycle = duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow