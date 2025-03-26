import heapq

from helpers.linked_list import ListNode


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if len(lists) == 0:
            return None

        min_heap: list[tuple[int, int, ListNode]] = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        D = ListNode()
        prev = D
        while min_heap:
            _, i, node = heapq.heappop(min_heap)
            prev.next = node
            prev = node

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        prev.next = None
        return D.next
