class Solution:
    # No division, prefix, suffix
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length of nums
        n = len(nums)

        # set list of 0's to same length of nums
        result = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        # nothing before first number, so prefix start with 1
        # nothing after last number, so suffix ends with 1
        prefix[0] = 1 
        suffix[ n - 1] = 1

        # build prefix product (left -> right)
        for i in range(1, n):
            # previous number * previous prefix product
            # stores product of everything BEFORE current index
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        # build suffix product (right -> left)
        for i in range(n - 2, -1, -1):
            # next number * next suffix product
            # stores product of everything AFTER current index
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        # multiply left product and right product together
        # gives product of every number except itself
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result