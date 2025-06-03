from collections import defaultdict
import heapq

import pytest


class HierholzerIter:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj: dict[str, list[str]] = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        stack: list[str] = ["JFK"]
        res: list[str] = []

        while stack:
            curr = stack[-1]
            if adj[curr]:
                stack.append(adj[curr].pop())
            else:
                res.append(stack.pop())

        return res[::-1]


class HierholzerRec:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Build a graph as an adjacency list
        flights_map: dict[str, list[str]] = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(flights_map[src], dst)

        trip_log: list[str] = []

        def dfs(src: str):
            while flights_map[src]:  # Process all destinations
                next_dst = heapq.heappop(flights_map[src])
                dfs(next_dst)
            trip_log.insert(0, src)  # Pre-order sorting of desintations

        dfs("JFK")
        return trip_log


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Build a graph as an adjacency list
        flights_map: dict[str, list[str]] = defaultdict(list)

        tickets.sort()
        for src, dest in tickets:
            flights_map[src].append(dest)

        trip_log = ["JFK"]

        def travel(src: str) -> bool:
            if len(trip_log) == len(tickets) + 1:
                return True

            if src not in flights_map:
                return False

            for i in range(len(flights_map[src].copy())):
                # Take ticket from flight map:
                dest = flights_map[src].pop(i)
                # Update trip log:
                trip_log.append(dest)

                # If we can complete itinerary using this path...
                if travel(dest):
                    return True

                # ...otherwise, undo taking the trip:
                flights_map[src].insert(i, dest)
                _ = trip_log.pop()

            # Unable to build a valid itinerary:
            return False

        _ = travel("JFK")
        return trip_log


@pytest.mark.parametrize(
    "tickets, answer",
    [
        (
            [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]],
            ["JFK", "BUF", "HOU", "SEA"],
        ),
    ],
)
def test_solution(tickets: list[list[str]], answer: list[str]):
    assert Solution().findItinerary(tickets) == answer
    assert HierholzerRec().findItinerary(tickets) == answer
    assert HierholzerIter().findItinerary(tickets) == answer
