class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary 'count' for frequency of each number
        count = {}

        # loop through every number
        for num in nums:
            # if number already exist + 1 to count of said number
            # if number dont exist, start at 0 for number and + 1
            count[num] = 1 + count.get(num, 0)
        
        # count now should look like this
        # {8: 2, 5: 3, 10: 1 }
        # number: freq
        
        arr = []
        for item in count.items():
            # reverse position of dictionary count
            num = item[0]
            cnt = item[1]
            arr.append([cnt, num])
            # now frequency belong to first slot
        arr.sort()
        # sort now freq are small to large

        # result
        res = []
        while len(res) < k:
            # pop(delete and return last digit = highest)
            # [1] get actual number skipping frequency, append to result
            res.append(arr.pop()[1])
        return res