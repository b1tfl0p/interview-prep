from collections import defaultdict


class HashSolution:
    """
    Time complexity: O(m * n)
    Space complexity: O(m)
    """

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict: dict[tuple[int, ...], list[str]] = defaultdict(list)
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord("a")] += 1
            anagram_dict[tuple(char_count)].append((s))
        return list(anagram_dict.values())


class SortedSolution:
    """
    Time complexity: O(m * nlog(n))
    Space complexity: O(m * n)
    """

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams: dict[str, list[str]] = defaultdict(list)

        for word in strs:
            word_key = "".join(sorted(word))
            anagrams[word_key].append(word)

        return list(anagrams.values())
