import pytest


class Solution:
    """
    Sliding Window + "HashMap"
    T: O(n)
    S: O(1)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Test for edge case:
        if len(s1) > len(s2):
            return False

        # Create "hashmaps" for the first len(s1) characters of each string:
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        l = 0  # left pointer

        # Iterate through the rest of s2:
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Introduce new character in window:
            idx = ord(s2[r]) - ord("a")
            s2_count[idx] += 1
            # Do the character counts match now?
            if s1_count[idx] == s2_count[idx]:
                matches += 1
            # Did the character counts match previously, but not anymore?
            elif s1_count[idx] + 1 == s2_count[idx]:
                matches -= 1

            # Remove left-most character from window:
            idx = ord(s2[l]) - ord("a")
            s2_count[idx] -= 1
            # Do the character counts match now?
            if s1_count[idx] == s2_count[idx]:
                matches += 1
            # Did the character counts match previously, but not anymore?
            elif s1_count[idx] - 1 == s2_count[idx]:
                matches -= 1

            # Shift the window:
            l += 1

        return matches == 26


@pytest.mark.parametrize(
    "s1, s2, answer",
    [
        ("abc", "lecabee", True),
        ("abc", "lecaabee", False),
    ],
)
def test_solution(s1: str, s2: str, answer: int) -> None:
    assert Solution().checkInclusion(s1, s2) == answer
