class PrefixSuffixSolution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Use two passes to calculate the end product at each index.
        # The first pass will calculate the product of all values that come before the specified index.
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # The second (reverse) pass will calculate the product of all values that come after the specified index.
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


class Solution:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                products[i] *= nums[j]
        return products
