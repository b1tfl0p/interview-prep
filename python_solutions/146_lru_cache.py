from collections import OrderedDict


class Node:
    def __init__(self, key: int, val: int):
        self.key: int = key
        self.val: int = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCacheDLL:
    def __init__(self, capacity: int):
        self.cap: int = capacity
        self.cache: dict[int, Node] = {}  # map key to node

        self.left: Node = Node(0, 0)
        self.right: Node = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev

    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        if prev:
            prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            if lru:
                self.remove(lru)
                del self.cache[lru.key]


class LRUCacheOD:
    """
    T: O(1) for each put() and get()
    S: O(n)
    """

    def __init__(self, capacity: int):
        self.cache: OrderedDict[int, int] = OrderedDict()
        self.cap: int = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            _ = self.cache.popitem(last=False)
