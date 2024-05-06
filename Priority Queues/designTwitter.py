# Problem: 355. Design Twitter

# Link: https://leetcode.com/problems/design-twitter/

# My Solution 1 - 
class Twitter:

    def __init__(self):
        self.sub = {}
        self.pq = {}
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.pq:
            self.pq[userId] = []
        self.pq[userId].append((self.t, tweetId))
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = self.pq[userId][-10:] if userId in self.pq else []
        if userId in self.sub:
            for u in self.sub[userId]:
                if u in self.pq:
                    pq += self.pq[u][-10:]
        heapify(pq)
        ans = []
        for i in range(10):
            if not pq:
                break
            ans.append(heappop(pq)[1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.sub:
            self.sub[followerId] = set()
        self.sub[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.sub:
            self.sub[followerId].discard(followeeId)

# Analysis:
# Runtime: O(k log(k)) - Where k is at most 10 * number of subscribers
#                        using priority queue
# Memory: O(n) - Where n is the total number of tweets, m for total number of followers 