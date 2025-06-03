from helpers.linked_list import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        prev = dummy
        carry = 0

        while l1 or l2 or carry:
            q, r = divmod(carry + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)

            carry = q if q else 0
            prev.next = ListNode(r)

            prev = prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
