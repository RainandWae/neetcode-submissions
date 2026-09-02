class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = []       # list of subarrays, split at every 0 (0 breaks any product chain)
        cur = []     # current subarray being built (no zeros inside)
        res = float('-inf')

        for num in nums:
            # track max even for lone zeros/single elements
            res = max(res, num)

            if num == 0:
                # hit a zero, close off current subarray, start fresh
                if cur:
                    A.append(cur)
                cur = []
            else:
                cur.append(num)

        # catch leftover subarray after loop ends
        if cur:
            A.append(cur)

        # process each zero-free subarray separately
        for sub in A:
            negs = sum(1 for i in sub if i < 0)  # count negative numbers in this subarray
            prod = 1

            # even number of negatives = all can be used (product stays positive)
            # odd number = must drop one negative to keep product positive, use one less
            need = negs if negs % 2 == 0 else negs - 1

            negs = 0  # reset, now used to count negatives seen so far in the window
            j = 0     # left pointer of window

            for i in range(len(sub)):
                prod *= sub[i]

                if sub[i] < 0:
                    negs += 1
                    # too many negatives in window, shrink from left until back within "need"
                    while negs > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j += 1

                # only valid if window hasn't collapsed past current index
                if j <= i:
                    res = max(res, prod)

        return res