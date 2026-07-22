class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negated = []  # separate list, don't overwrite original input
        for s in stones:
            # python heapq is only minheap, negate values so it maxheap
            # smallest negative = biggest original number
            negated.append(-s)

        stones = negated
        heapq.heapify(stones)  # turn list into heap structure, O(n)

        while len(stones) > 1:
            # pop 2 biggest stones (smallest negatives = biggest originals)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # note: since these are negated, "second > first" means
            # second's original value is actually smaller
            if second > first:
                # smash them together, push the difference back (still negated)
                heapq.heappush(stones, first - second)

        stones.append(0)  # edge case: if all stones destroyed, list is empty, avoid index error
        return abs(stones[0])  # undo the negation, get final weight