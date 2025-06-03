import pytest


class ManacherAlgo:
    def countSubstrings(self, s: str) -> int:
        t = f"^#{'#'.join(s)}#$"
        p = [0] * len(t)
        l, r = 1, 2
        for i in range(1, len(t) - 1):
            p[i] = max(0, min(r - i, p[l + (r - i)]))

            while t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > r:
                l = i - p[i]
                r = i + p[i]

        return sum(((x + 1) // 2 for x in p))


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPali(s, i, i)
            count += self.countPali(s, i, i + 1)
        return count

    def countPali(self, s: str, left: int, right: int) -> int:
        count = 0
        while 0 <= left and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count


@pytest.mark.parametrize(
    "s, answer",
    [
        ("abc", 3),
        ("aaa", 6),
    ],
)
def test_solution(s: str, answer: int):
    assert Solution().countSubstrings(s) == answer
    assert ManacherAlgo().countSubstrings(s) == answer


if __name__ == "__main__":
    m = ManacherAlgo()
    # m.countSubstrings("aaa")
    m.countSubstrings("babcbabcbaccba")
