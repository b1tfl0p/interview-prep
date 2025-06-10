import pytest


class BacktrackSolution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        subset: list[int] = []

        def dfs(i: int) -> None:
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            _ = subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


class IterationSolution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = [[]]

        for n in nums:
            res += [subset + [n] for subset in res]

        return res


class BitManipulationSolution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res: list[list[int]] = []
        for i in range(1 << n):
            subset = [nums[j] for j in range(n) if (i & 1 << j)]
            res.append(subset)
        return res


@pytest.mark.parametrize(
    argnames="nums, answer",
    argvalues=[
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    ],
)
def test_solutions(nums: list[int], answer: list[list[int]]) -> None:
    bts = sorted(BacktrackSolution().subsets(nums), key=len)
    print("bts:", bts)
    print("answer:", answer)
    assert bts == answer
    assert IterationSolution().subsets(nums) == answer
    assert BitManipulationSolution().subsets(nums) == answer
