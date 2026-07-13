class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        # turn [8,4,2,6] ==> [[8, 0],[4, 1],[2, 2],[6, 3]]
        # tagging index position to numbers

        A.sort()
        # sort entire list from small->big
        # [[2, 2],[4, 1],[6, 3],[8, 0]]
        
        i = 0
        j = len(nums) - 1
        while i < j:
            # current sum of two number checked
            cur = A[i][0] + A[j][0]
            # check if
            if cur == target: 
                # yes then return indeces of orignal value(bc asked for incides)
                return [min(A[i][1], A[j][1]),
                    max(A[i][1], A[j][1])]
            
            # if target still greater than current, move i right
            elif cur < target:
                i += 1
            # current is greater then reduce j, move left
            else: 
                j -= 1
        # all fail return nothing
        return []
