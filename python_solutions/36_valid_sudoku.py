class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows: list[set[str]] = [set() for _ in range(9)]
        cols: list[set[str]] = [set() for _ in range(9)]
        sqrs: list[set[str]] = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val: str = board[r][c]
                if val == ".":
                    continue

                s: int = ((r // 3) * 3) + (c // 3)

                if val in rows[r] or val in cols[c] or val in sqrs[s]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                sqrs[s].add(val)

        return True
