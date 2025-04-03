import math


class Solution:
    """
    Be careful dividing negative numbers!
    """

    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        rev = 0
        while x:
            mod = int(math.fmod(x, 10))
            x = int(x / 10)

            if (
                rev > MAX // 10
                or rev < int(MIN / 10)
                or (rev == MAX // 10 and mod > MAX % 10)
                or (rev == int(MIN / 10) and mod < int(math.fmod(MIN, 10)))
            ):
                return 0

            rev = (rev * 10) + mod

        return rev
