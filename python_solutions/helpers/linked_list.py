from typing import Self, final


@final
class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None) -> None:
        self.val = val
        self.next = next


def build_linked_list(vals: list[int]) -> ListNode | None:
    if not vals:
        return None

    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head
