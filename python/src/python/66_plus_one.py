import pytest


class OptimalSolution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Notice that we will only have a carry when digit[i] == 9
        for i in range(len(digits) - 1, -1, -1):
            print(f"i: {i}, digits[i]: {digits[i]}")
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we get to this point, we need to add a 1 to the front of the list:
        return [1] + digits


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        i = len(digits) - 1
        while carry and 0 <= i:
            sum = digits[i] + carry
            carry = sum // 10
            digits[i] = sum % 10
            i -= 1

        if carry:
            digits.insert(0, carry)

        return digits


@pytest.mark.parametrize(
    "input, answer",
    [
        ([1, 2, 3, 4], [1, 2, 3, 5]),
        ([9, 9, 9], [1, 0, 0, 0]),
    ],
)
def test_solution(input: list[int], answer: list[int]):
    assert Solution().plusOne(input.copy()) == answer
    assert OptimalSolution().plusOne(input.copy()) == answer
