class Solution:
    """
    Control the beginning of the encoded string with formatted metadata.
    In this case, the length of the next string followed by a delimiter (#).
    Any '#' character that appears in the tokens themselves will be skipped over.
    T: O(m)
    S: O(m + n)
    where m is the sum of the length of all strings and n is the number of strings
    (to account for the approximate number of times the delimiter appears)
    """

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> list[str]:
        res: list[str] = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
