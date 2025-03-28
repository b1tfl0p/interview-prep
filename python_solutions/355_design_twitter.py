import heapq
from collections import defaultdict

import pytest


class Twitter:
    def __init__(self) -> None:
        self.recency: int = 0
        self.userTweets: dict[int, list[list[int]]] = defaultdict(list)
        self.followsMap: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.userTweets[userId]) == 10:
            _ = self.userTweets[userId].pop(0)

        self.userTweets[userId].append([self.recency, tweetId])
        self.recency -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        feed: list[int] = []
        minHeap: list[list[int]] = []

        self.followsMap[userId].add(userId)
        for followeeId in self.followsMap[userId]:
            if followeeId in self.userTweets:
                next_index = len(self.userTweets[followeeId]) - 1
                recency, tweetId = self.userTweets[followeeId][next_index]
                heapq.heappush(minHeap, [recency, tweetId, followeeId, next_index - 1])

        while minHeap and len(feed) < 10:
            _, tweetId, followeeId, next_index = heapq.heappop(minHeap)
            feed.append(tweetId)
            if next_index >= 0:
                recency, tweetId = self.userTweets[followeeId][next_index]
                heapq.heappush(minHeap, [recency, tweetId, followeeId, next_index - 1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followsMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followsMap[followerId].discard(followeeId)


@pytest.mark.parametrize(
    "commands, answers",
    [
        (
            [
                "Twitter",
                "postTweet",
                [1, 10],
                "postTweet",
                [2, 20],
                "getNewsFeed",
                [1],
                "getNewsFeed",
                [2],
                "follow",
                [1, 2],
                "getNewsFeed",
                [1],
                "getNewsFeed",
                [2],
                "unfollow",
                [1, 2],
                "getNewsFeed",
                [1],
            ],
            [None, None, None, [10], [20], None, [20, 10], [20], None, [10]],
        )
    ],
)
def test_solution(commands, answers):
    t: Twitter = globals()[commands[0]]()
    a = 1
    for i in range(1, len(commands), 2):
        assert getattr(t, commands[i])(*(commands[i + 1])) == answers[a]
        a += 1
