from collections import deque
import heapq

import pytest


class DijkstrasSolution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        """
        Parameters
        ----------
        n : int
            number of cities
        flights : list[list[int]] : len(list[int]) == 3
            list of flights where each flight is stored as list
            [[source, destination, price], ...]
        src : int
            the starting airport
        dst : int
            the destination airport
        k : int
            the maximum number of stops you can make (not including `src` and `dst`)

        Returns
        -------
        int
            the cheapest price from `src` to `dst` with at most `k` stops, or `-1` if
            there is no such route
        """
        INF = float("inf")
        adj: list[list[list[int]]] = [[] for _ in range(n)]
        dist = [[INF] * (k + 5) for _ in range(n)]

        for u, v, w in flights:
            adj[u].append([v, w])

        dist[src][0] = 0
        minHeap = [(0, src, -1)]  # cost, node, stops

        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node:
                return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue

            for v, w in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                if dist[v][nextStops + 1] > nextCst:
                    dist[v][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, v, nextStops))

        return -1


class BellmanFordSolution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # 1. Initialization:
        # Set the price to the source vertex to 0 and all other vertices to
        # infinity.
        prices = [float("inf")] * n
        prices[src] = 0

        # 3. Iteration:
        # Repeat the relaxation step for all edges k + 1 times.
        for _ in range(k + 1):
            updated_prices = prices.copy()

            # 2. Relaxation:
            # For each edge (u, v) with weight (w),...
            for u, v, w in flights:
                # ...if the price to v is greater than the price to u plus w...
                if prices[u] != float("inf") and prices[u] + w < updated_prices[v]:
                    # ...update the price to v.
                    updated_prices[v] = prices[u] + w

            prices = updated_prices

        return int(prices[dst]) if prices[dst] != float("inf") else -1


class ShortestPathFasterSolution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj: list[list[list[int]]] = [[] for _ in range(n)]

        for u, v, w in flights:
            adj[u].append([v, w])

        q = deque([(0, src, 0)])
        while q:
            cost, u, stops = q.popleft()
            if stops > k:
                continue

            for v, w in adj[u]:
                nextCost = cost + w
                if nextCost < prices[v]:
                    prices[v] = nextCost
                    q.append((nextCost, v, stops + 1))

        return int(prices[dst]) if prices[dst] != float("inf") else -1


@pytest.mark.parametrize(
    argnames="n, flights, src, dst, k, answer",
    argvalues=[
        (
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
            700,
        ),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    ],
)
def test_solution(
    n: int, flights: list[list[int]], src: int, dst: int, k: int, answer: int
) -> None:
    assert DijkstrasSolution().findCheapestPrice(n, flights, src, dst, k) == answer
    assert BellmanFordSolution().findCheapestPrice(n, flights, src, dst, k) == answer
    assert (
        ShortestPathFasterSolution().findCheapestPrice(n, flights, src, dst, k)
        == answer
    )
