class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count occurrences of each task
        count = Counter(tasks)
        # negate counts for maxheap, most frequent task popped first
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        # holds tasks on cooldown, pairs of [-cnt, idleTime]
        q = deque()

        # keep going while theres tasks left to schedule OR tasks still cooling down
        while maxHeap or q:
            time += 1

            if not maxHeap:
                # nothing to do right now, fast-forward time to when next task is ready
                time = q[0][1]
            else:
                # pop most frequent task, do it once
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    # still has remaining count, put on cooldown until time + n
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                # cooldown finished for front of queue, push back into heap
                heapq.heappush(maxHeap, q.popleft()[0])

        return time