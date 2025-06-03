from collections import defaultdict


class DetectSquares:
    """
    Hash Map: { x: {y : count}}
    T: O(1) for add; O(n) for count
    S: O(n)
    """

    def __init__(self):
        self.pts_count: dict[int, dict[int, int]] = defaultdict(
            lambda: defaultdict(int)
        )

    def add(self, point: list[int]) -> None:
        self.pts_count[point[0]][point[1]] += 1

    def count(self, point: list[int]) -> int:
        res = 0
        x1, y1 = point

        for y2 in self.pts_count[x1]:
            side = y2 - y1

            if side == 0:
                continue

            x3, x4 = x1 + side, x1 - side
            res += (
                self.pts_count[x1][y2] * self.pts_count[x3][y1] * self.pts_count[x3][y2]
            )
            res += (
                self.pts_count[x1][y2] * self.pts_count[x4][y1] * self.pts_count[x4][y2]
            )

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
