from collections import deque
import pytest


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        minutes = 0
        fresh = 0
        rotten_oranges: deque[tuple[int, int]] = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten_oranges.append((r, c))

        while fresh and rotten_oranges:
            length = len(rotten_oranges)
            for _ in range(length):
                r, c = rotten_oranges.popleft()
                for dr, dc in DIRS:
                    row, col = r + dr, c + dc

                    if (
                        row in range(NUM_ROWS)
                        and col in range(NUM_COLS)
                        and grid[row][col] == 1
                    ):
                        fresh -= 1
                        grid[row][col] = 2
                        rotten_oranges.append((row, col))

            minutes += 1

        return minutes if fresh == 0 else -1


@pytest.mark.parametrize(
    argnames="grid, answer",
    argvalues=[
        ([[1, 1, 0], [0, 1, 1], [0, 1, 2]], 4),
        ([[1, 0, 1], [0, 2, 0], [1, 0, 1]], -1),
    ],
)
def test_solution(grid: list[list[int]], answer: int) -> None:
    assert Solution().orangesRotting(grid) == answer
