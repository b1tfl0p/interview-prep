class FastSlowPointerSolution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)

        return fast == 1

    def sumOfSquares(self, n: int) -> int:
        sum = 0

        while n:
            sum += (n % 10) ** 2
            n //= 10

        return sum


class HashSetSolution:
    def isHappy(self, n: int) -> bool:
        seen: set[int] = set()

        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True

        return False

    def sumOfSquares(self, n: int) -> int:
        sum = 0

        while n:
            sum += (n % 10) ** 2
            n //= 10

        return sum


def test_Solution():
    hs = HashSetSolution()
    fs = FastSlowPointerSolution()

    tests = [(19, True), (2, False)]

    for input, output in tests:
        assert fs.isHappy(input) == output
        assert hs.isHappy(input) == output
