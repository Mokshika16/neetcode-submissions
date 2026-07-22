from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId):
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(heap, (time, tweetId, followee, index - 1))

        while heap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(heap, (time, tweetId, followee, index - 1))

        return res

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)