import pytest


class Optimal:
    """
    T: O(n)
    S: O(m)
    where 'n' is the length of the string
    and 'm' is the total number of unique characters in the string
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        mp: dict[
            str, int
        ] = {}  # character to the index of the last instance of the character
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest


class Solution:
    """
    T: O(n)
    S: O(m)
    where 'n' is the length of the string
    and 'm' is the total number of unique characters in the string
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        l = 0
        r = 0
        char_set: set[str] = set(s[l])

        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
            else:
                char_set.remove(s[l])
                l += 1

            if len(char_set) > longest:
                longest = len(char_set)

        return longest


@pytest.mark.parametrize(
    "s, answer",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_solution(s: str, answer: int):
    assert Solution().lengthOfLongestSubstring(s) == answer
    assert Optimal().lengthOfLongestSubstring(s) == answer
