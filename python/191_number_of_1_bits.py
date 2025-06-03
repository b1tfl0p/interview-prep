import pytest


class Optimal:
    """
    Using this trick, you only go through the loop the
    same number of times as there are 1's in the number.

    Effectively you eliminate the rightmost 1 bit each loop and skip over all the 0s.
    """

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        while n:
            bit_count += n & 1
            n >>= 1
        return bit_count


@pytest.mark.parametrize(
    "n, answer",
    [
        (11, 3),
        (128, 1),
    ],
)
def test_solution(n: int, answer: int):
    assert Solution().hammingWeight(n) == answer
    assert Optimal().hammingWeight(n) == answer
