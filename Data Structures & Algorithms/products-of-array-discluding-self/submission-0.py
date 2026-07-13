class Solution:
    # Brute Force
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length of list
        n = len(nums)

        #set list of 0's same length as nums
        res = [0] * n

        # loop through entire nums
        for i in range(n): 
            # set base for multiply
            prod = 1 
            for j in range(n):
                if i == j:
                    continue # skip itself
                prod *= nums[j]
                # multiply all of j's

            res[i] = prod
            # replace 0 in 'i' position with prod
        return res