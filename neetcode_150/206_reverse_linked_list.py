from typing import Self, final


@final
class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next


def list_to_ll(vals: list[int]) -> ListNode | None:
    if len(vals) == 0:
        return None

    head = ListNode(vals.pop(0))
    prev: ListNode | None = head
    curr: ListNode | None = None
    for val in vals:
        curr = ListNode(val)
        if prev:
            prev.next = curr
        prev = curr

    return head


def ll_to_list(head: ListNode | None) -> list[int]:
    if not head:
        return []
    res: list[int] = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class RecursiveSolution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead


class IterativeSolution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """
        >>> ll_to_list(IterativeSolution().reverseList(list_to_ll([1,2,3,4,5])))
        [5, 4, 3, 2, 1]
        """
        prev, curr = None, head
        while curr:
            next, curr.next = curr.next, prev
            prev, curr = curr, next

        return prev


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
