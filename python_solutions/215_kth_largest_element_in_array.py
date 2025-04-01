import heapq


class QuickSelect:
    """
    T: O(n) average [O(n^2) worst case]
    S: O(n)
    """

    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l: int, r: int) -> int:
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


class Solution:
    """
    Use a min heap of size 'k' to find the 'k'th largest element:
    T: O(n log k)
    S: O(k)
    where 'n' is the length of the array
    """

    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap: list[int] = nums[:k]
        heapq.heapify(min_heap)
        for n in nums[k:]:
            _ = heapq.heappushpop(min_heap, n)
        return min_heap[0]
