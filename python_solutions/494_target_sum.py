from collections import defaultdict

import pytest


class DynamicOptimized:
    """
    1. Iterate through list of numbers.
    2. Keep track of the sums possible and how many times a sum appears
       using a hashmap making sure to create a new HashMap at each iteration
       (we only care about the latest hashmap).
    3. Use the built hashmap to find how many times the target sum appeared.
    """

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # intermediate sum -> # of times it can be made
        dp: dict[int, int] = defaultdict(int)
        dp[0] = 1  # 1 way to get the sum = 0...for now

        for num in nums:
            new_dp: dict[int, int] = defaultdict(int)

            # for each sum and count we have accumulated so far...
            for total, count in dp.items():
                # ...add new sums to the hashmap and update their count values
                new_dp[total + num] += count
                new_dp[total - num] += count
            # replace the old hashmap with the updated sums and counts
            dp = new_dp

        # check the hashmap for how many ways
        # we are able to make the target sum:
        return dp[target]


class DynamicTD:
    """
    Backtracking and Memoization using a HashMap

    T: O(n * m)
    S: O(n * m)

    where n is the length of the array nums and m is the sum of all the elements in the array
    """

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp: dict[tuple[int, int], int] = {}  # (index, total) -> # of ways

        def backtrack(i: int, cur_sum: int) -> int:
            if i == len(nums):
                return 1 if cur_sum == target else 0

            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]

            dp[(i, cur_sum)] = backtrack(i + 1, cur_sum + nums[i]) + backtrack(
                i + 1, cur_sum - nums[i]
            )

            return dp[(i, cur_sum)]

        return backtrack(0, 0)


class MySolution:
    """
    Runs too long and can overflow the stack with a large enough list
    """

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        valid_sums = 0

        def dfs(nums: list[int], running_sum: int) -> None:
            if not nums:
                if running_sum == target:
                    nonlocal valid_sums
                    valid_sums += 1
            else:
                n, *tail = nums

                dfs(tail, running_sum + n)
                dfs(tail, running_sum - n)

        dfs(nums, 0)
        return valid_sums


@pytest.mark.parametrize(
    "nums, target, answer",
    [
        ([1], -1, 1),
        ([2, 2, 2], 2, 3),
        ([1, 1, 1, 1, 1], 3, 5),
        (
            [
                34,
                21,
                12,
                36,
                16,
                7,
                31,
                7,
                41,
                49,
                7,
                48,
                22,
                19,
                32,
                46,
                19,
                18,
                44,
                34,
            ],
            47,
            5705,
        ),
    ],
)
def test_solution(nums: list[int], target: int, answer: int) -> None:
    assert MySolution().findTargetSumWays(nums, target) == answer
    assert DynamicTD().findTargetSumWays(nums, target) == answer
    assert DynamicOptimized().findTargetSumWays(nums, target) == answer
