import pytest


class Solution:
    """
    Build adjacency list mapping courses to their pre-reqs.
    T: O(V + E)
    S: O(V + E
    """

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Map all courses to their pre-reqs:
        c_to_pre: list[list[int]] = [[] for _ in range(numCourses)]
        for c, pre in prerequisites:
            c_to_pre[c].append(pre)

        # Store the pre-req courses we visit when evaluating a course:
        visited: set[int] = set()

        def dfs(c: int) -> bool:
            if c in visited:
                # Cycle detected:
                return False
            if c_to_pre[c] == []:
                return True

            visited.add(c)
            for pre in c_to_pre[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)

            # c (and all it's prereqs) can be completed:
            c_to_pre[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


@pytest.mark.parametrize(
    "numCourses, prerequisites, answer",
    [(2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False)],
)
def test_solution(
    numCourses: int, prerequisites: list[list[int]], answer: bool
) -> None:
    assert Solution().canFinish(numCourses, prerequisites) == answer
