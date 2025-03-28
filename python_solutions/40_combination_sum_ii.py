import pytest


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        combos: list[list[int]] = []
        candidates.sort()

        def dfs(i: int, cur_sum: int, taken: list[int]):
            # Base condition: cur_sum is equal to the target:
            if cur_sum == target:
                combos.append(taken.copy())
                return
            # Base condition: remaining sums are larger than target
            if cur_sum > target or i == len(candidates):
                return

            # Take value:
            dfs(i + 1, cur_sum + candidates[i], taken + [candidates[i]])

            # Ignore value:
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur_sum, taken)

        dfs(0, 0, [])
        return combos


@pytest.mark.parametrize(
    "candidates, target, answer",
    [
        ([9, 2, 2, 4, 6, 1, 5], 8, [[1, 2, 5], [2, 2, 4], [2, 6]]),
        ([1, 2, 3, 4, 5], 7, [[1, 2, 4], [2, 5], [3, 4]]),
    ],
)
def test_solution(candidates: list[int], target: int, answer: list[list[int]]) -> None:
    assert Solution().combinationSum2(candidates, target) == answer
