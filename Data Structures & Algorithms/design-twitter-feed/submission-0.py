class Twitter:
    def __init__(self):
        # global counter, decreases with every tweet, 
        # acts as timestamp (newer = smaller/more negative)
        self.count = 0
        # userId -> list of [count, tweetId], tweets stored in order posted
        self.tweetMap = defaultdict(list)
        # userId -> set of followeeId
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # store tweet with current count as "timestamp"
        self.tweetMap[userId].append([self.count, tweetId])
        # decrement so next tweet has smaller count 
        # ==> pops first in minheap (most recent = smallest number)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # user follows themself too, so their own tweets show up in feed
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # start from the most recent tweet (last index) of each followee
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # push most recent tweet from this followee, track index to grab next one later
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # pop from heap, always getting the most recent tweet across all followees
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # if this followee has older tweets left, push the next one in
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # only remove if actually following them
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)