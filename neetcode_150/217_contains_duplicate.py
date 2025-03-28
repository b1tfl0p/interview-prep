class Solution:
    # "Hash Set" solution
    # T: O(n)
    # S: O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        s: set[int] = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False


class AlternativeSolution:
    # "Hash Set Length" solution
    # T: O(n)
    # S: O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)


def test_Solutions():
    s = Solution()
    s_1 = AlternativeSolution()

    tests = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]

    for nums, answer in tests:
        assert s.containsDuplicate(nums) == answer
        assert s_1.containsDuplicate(nums) == answer
