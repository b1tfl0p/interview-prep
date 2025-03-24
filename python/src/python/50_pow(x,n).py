import pytest


class BinaryExponentiation:
    """
    T: O(log n)
    S: O(1)
    """

    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power:
            if power & 1:
                res *= x
            x *= x
            power >>= 1

        return res if n >= 0 else 1 / res


class BruteForceSoluiton:
    """
    T: O(n)
    S: O(1)
    """

    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        result = 1
        for _ in range(abs(n)):
            result *= x
        return result if n > 0 else 1 / result


@pytest.mark.parametrize(
    "base, exponent, answer",
    [
        (2.00000, 5, 32.00000),
        (1.10000, 10, 2.59374),
        (2.00000, -3, 0.12500),
    ],
)
def test_solution(base: float, exponent: int, answer: float):
    assert f"{BruteForceSoluiton().myPow(base, exponent):.{5}}" == f"{answer:.{5}}"
    assert f"{BinaryExponentiation().myPow(base, exponent):.{5}}" == f"{answer:.{5}}"
