import pytest


class Solution:
    """
    Two Pointers
    T: O(n)
    S: O(1)
    """

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        # Unreachable:
        return []


@pytest.mark.parametrize(
    "nums, target, answer",
    [
        ([1, 2, 3, 4], 3, [1, 2]),
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ],
)
def test_solution(nums: list[int], target: int, answer: list[int]) -> None:
    assert Solution().twoSum(nums, target) == answer
