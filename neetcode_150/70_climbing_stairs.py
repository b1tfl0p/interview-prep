class Solution:
    def climbStairs(self, n: int) -> int:
        # Use dynamic programming to keep track of the number of ways you can get to each individual step.
        #
        # INFO: Notice that this is actually the Fibonacci sequence!
        #
        # Edge cases:
        # n = 1, 2 or 3
        if n <= 3:
            return n

        one, two = 3, 2

        for _ in range(3, n):
            temp = one
            one = one + two
            two = temp

        return one


def test_climbStairs():
    s = Solution()
    # Edge cases:
    assert s.climbStairs(1) == 1
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3

    assert s.climbStairs(5) == 8
    assert s.climbStairs(8) == 34
