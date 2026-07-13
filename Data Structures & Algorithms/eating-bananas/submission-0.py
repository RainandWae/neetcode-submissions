# Binary Search
# k = banana per hour, assuming k = integer(whole number)
# Bigger k = eat faster = fewer hours needed.
# Smaller k = slower = more hours needed.
# k go up, hours needed go down.
# mean "only one direction" behaviour
# ==> so make it efficient, we do binary search
# pick middle k, if <= hour, go smaller or bigger k
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # lowest k
        r = max(piles)
        result = r # highest k

        while l <= r:
            k = (l + r) // 2 # set middle k

            totalTime = 0
            for p in piles:
                # round up to nearest integer(whole number)
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                result = k
                r = k - 1
            else:
                l = k + 1
        return result