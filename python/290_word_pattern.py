from itertools import zip_longest


def wordPattern(pattern: str, s: str) -> bool:
    """
    >>> wordPattern("e", "eukera")
    True
    """
    words = s.split(" ")
    return (
        len(set(pattern))
        == len(set(words))
        == len(
            set(
                zip_longest(
                    pattern,
                    words,
                )
            )
        )
    )


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
