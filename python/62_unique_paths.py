import pytest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                memo[c] += memo[c - 1]

        return memo[-1]


@pytest.mark.parametrize(
    "m, n, answer",
    [
        (3, 7, 28),
        (3, 2, 3),
    ],
)
def test_solution(m: int, n: int, answer: int):
    assert Solution().uniquePaths(m, n) == answer
