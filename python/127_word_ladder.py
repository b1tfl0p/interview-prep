from collections import defaultdict, deque

import pytest


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        adj: dict[str, set[str]] = defaultdict(set)
        word_patterns: dict[str, set[str]] = defaultdict(set)

        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                key = word[:j] + "*" + word[j + 1 :]
                adj[key].add(word)
                word_patterns[word].add(key)

        # Perform BFS:
        visited: set[str] = set()
        q = deque([beginWord])
        distance = 1
        while q:
            # Keep track of when we move to the next level in the graph:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return distance

                for pattern in word_patterns[word]:
                    for next_word in adj[pattern]:
                        if next_word not in visited:
                            visited.add(word)
                            q.append(next_word)

            distance += 1

        # No path found:
        return 0


@pytest.mark.parametrize(
    "beginWord, endWord, wordList, answer",
    [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ],
)
def test_solution(beginWord, endWord, wordList, answer):
    assert Solution().ladderLength(beginWord, endWord, wordList) == answer
