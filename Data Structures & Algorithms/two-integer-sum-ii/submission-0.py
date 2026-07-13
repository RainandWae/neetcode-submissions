# TWO POINTER
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1

        # loop until reach middle
        # avoid using same element twice
        # since l will always be less than r
        while l < r:
            # get current sum of two pointer value
            curSum = numbers[l] + numbers[r]

            # if sum is over target move right pointer left
            if curSum > target:
                r -= 1
            
            # if sum is under target move left pointer right
            elif curSum < target:
                l += 1
            
            # found two sum equal to target return
            else:
                return [l + 1, r + 1]
        return []