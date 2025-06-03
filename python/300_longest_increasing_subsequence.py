import pytest


class Solution:
    """
    T: O(n^2)
    S: O(n)
    """

    # Dynamic Programming (Bottom-Up)
    def lengthOfLIS(self, nums: list[int]) -> int:
        longest = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    longest[i] = max(longest[i], 1 + longest[j])
        return max(longest)


@pytest.mark.parametrize(
    "input, answer",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ],
)
def test_solution(input: list[int], answer: int) -> None:
    assert Solution().lengthOfLIS(input) == answer
