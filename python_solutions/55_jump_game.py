class Solution:
    """
    Greedy algorithm.
    T: O(n)
    S: O(1)
    """

    def canJump(self, nums: list[int]) -> bool:
        steps_remaining = 0
        for steps_allowed in nums:
            if steps_remaining < 0:
                return False
            steps_remaining = max(steps_remaining, steps_allowed)
            steps_remaining -= 1
        return True
