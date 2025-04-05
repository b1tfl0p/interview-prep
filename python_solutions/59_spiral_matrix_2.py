import pytest


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bot, left, right = 0, n - 1, 0, n - 1
        val = 1
        while val <= n * n:
            # Fill top row left to right:
            for i in range(left, right + 1):
                matrix[top][i], val = val, val + 1
            top += 1
            # Fill right col top to bot:
            for i in range(top, bot + 1):
                matrix[i][right], val = val, val + 1
            right -= 1
            # Fill bot row right to left:
            for i in range(right, left - 1, -1):
                matrix[bot][i], val = val, val + 1
            bot -= 1
            # Fill left col bot to top:
            for i in range(bot, top - 1, -1):
                matrix[i][left], val = val, val + 1
            left += 1
        return matrix


@pytest.mark.parametrize(
    "n, answer",
    [
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (2, [[1, 2], [4, 3]]),
        (1, [[1]]),
    ],
)
def test_solution(n: int, answer: list[list[int]]):
    assert Solution().generateMatrix(n) == answer


if __name__ == "__main__":
    res = Solution().generateMatrix(2)
    print(res)
