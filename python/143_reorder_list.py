import pytest

from helpers.linked_list import ListNode, build_linked_list


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Get a pointer to the middle of the list:
        slow = head
        fast = head.next

        while fast and fast.next:
            assert slow
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list:
        assert slow
        reverse = slow.next
        prev = slow.next = None
        while reverse:
            tmp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = tmp

        assert prev
        # Zip the two lists together:
        h1 = head
        h2 = prev
        while h2:
            assert h1
            t1, t2 = h1.next, h2.next
            h1.next = h2
            h2.next = t1
            h1, h2 = t1, t2


@pytest.mark.parametrize(
    "head, answer", [([1, 2, 3, 4], [1, 4, 2, 3]), ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])]
)
def test_solution(head: list[int], answer: list[int]):
    ll = build_linked_list(head)
    if not ll:
        assert False
    Solution().reorderList(ll)
    res: list[int] = []
    while ll:
        res.append(ll.val)
        ll = ll.next
    assert res == answer
