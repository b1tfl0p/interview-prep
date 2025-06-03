import pytest


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS * COLS - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = mid // COLS, mid % COLS
            if target < matrix[row][col]:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True
        return False


@pytest.mark.parametrize(
    "matrix, target, answer",
    [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ],
)
def test_solution(matrix: list[list[int]], target: int, answer: bool):
    assert Solution().searchMatrix(matrix, target) == answer

