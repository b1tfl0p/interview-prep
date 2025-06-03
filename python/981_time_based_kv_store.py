import bisect
from collections import defaultdict


class TimeMapNoBisect:
    def __init__(self):
        self.kv: dict[str, list[tuple[str, int]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int):
        # Assuming timestamps come in increasing order:
        self.kv[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.kv[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


class TimeValue:
    def __init__(self):
        self.timestamps: list[int] = []
        self.values: dict[int, str] = defaultdict(str)


class TimeMap:
    def __init__(self):
        self.kv: dict[str, TimeValue] = defaultdict(TimeValue)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.kv[key].timestamps, timestamp)
        self.kv[key].values[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect_right(self.kv[key].timestamps, timestamp)
        if i:
            t = self.kv[key].timestamps[i - 1]
            return self.kv[key].values[t]
        return ""
