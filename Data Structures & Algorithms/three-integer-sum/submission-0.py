class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # store final answer
        result = []

        # sort so we can use two pointers
        nums.sort()

        # choose one number at a time
        for i in range(len(nums)):
            a = nums[i] # current number

            # if first number is already positive,
            # remaining numbers are also positive
            # impossible to make sum = 0
            if a > 0:
                break

            # skip duplicate first numbers
            if i > 0 and a == nums[i - 1]:
                continue

            # two pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                # sum of the three numbers
                threeSum = a + nums[l] + nums[r]

                # sum too big, move right pointer left
                if threeSum > 0:
                    r -= 1

                # sum too small, move left pointer right
                elif threeSum < 0:
                    l += 1

                # found three numbers that sum to 0
                else:
                    result.append([a, nums[l], nums[r]])

                    # continue searching
                    l += 1
                    r -= 1

                    # skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        # return all unique triplets
        return result