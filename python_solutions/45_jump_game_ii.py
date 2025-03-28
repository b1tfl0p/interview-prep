import pytest


class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1

        return jumps


@pytest.mark.parametrize("nums, answer", [([2, 4, 1, 1, 1, 1], 2)])
def test_solution(nums, answer):
    assert Solution().jump(nums) == answer
