class Solution:
    def findKthLargest(self, nums, k):
        # take first kth element, so heap have size k
        heap = nums[:k]

        # turn into min heap, heap[0]= smallest of these k
        heapq.heapify(heap)

        # go through the rest of the elements
        for n in nums[k:]:
            # bigger than smallest in heap? it belongs in top-k
            if n > heap[0]:
                # pop smallest, push n (does both in one step)
                heapq.heapreplace(heap, n)
        # smallest item left in heap = kth largest overall
        return heap[0]