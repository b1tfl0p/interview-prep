import pytest


class Solution:
    """
    If truncating towards 0, then you cannot simply do floor division (//)
    since negative numbers will truncate away from zero. Use int() instead.
    T: O(n)
    S: O(n)
    """

    def evalRPN(self, tokens: list[str]) -> int:
        s: list[int] = []
        for t in tokens:
            if t == "+":
                a = s.pop()
                b = s.pop()
                s.append(b + a)
            elif t == "-":
                a = s.pop()
                b = s.pop()
                s.append(b - a)
            elif t == "*":
                a = s.pop()
                b = s.pop()
                s.append(b * a)
            elif t == "/":
                a = s.pop()
                b = s.pop()
                s.append(int(b / a))
            else:
                s.append(int(t))
        return s[0]


@pytest.mark.parametrize(
    "tokens, answer",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_solution(tokens, answer):
    assert Solution().evalRPN(tokens) == answer
