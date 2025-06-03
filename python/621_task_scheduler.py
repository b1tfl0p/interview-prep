from collections import Counter, deque
import heapq
import pytest


class MathSolution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord("A")] += 1

        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)


class GreedySolution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord("A")] += 1

        count.sort()
        maxf = count[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(maxf - 1, count[i])
        return max(0, idle) + len(tasks)


class MaxHeapSolution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapq.heapify(max_heap)

        tick: int = 0
        timeout_queue: deque[list[int]] = deque()  # pairs of [-count, idle_time]
        while max_heap or timeout_queue:
            tick += 1

            if not max_heap:
                # Fast forward tick to when there is available work:
                tick = timeout_queue[0][1]
            else:
                # Process the task with the highest count:
                count = 1 + heapq.heappop(max_heap)
                # If there are more tasks of this type to process...
                if count:
                    # ...hold it in the timeout queue until the interval lapses:
                    timeout_queue.append([count, tick + n])

            if timeout_queue and timeout_queue[0][1] == tick:
                # Re-add the task into the max_heap for
                # processing now that the interval has elapsed:
                heapq.heappush(max_heap, timeout_queue.popleft()[0])

        return tick


@pytest.mark.parametrize(
    "tasks, n, answer",
    [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "C", "A", "B", "D", "B"], 1, 6),
        (["A", "A", "A", "B", "B", "B"], 3, 10),
    ],
)
def test_solution(tasks: list[str], n: int, answer: int):
    assert MaxHeapSolution().leastInterval(tasks, n) == answer
    assert GreedySolution().leastInterval(tasks, n) == answer
    assert MathSolution().leastInterval(tasks, n) == answer
