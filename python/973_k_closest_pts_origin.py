import heapq


class HeapqSolution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)


class SortSolution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
