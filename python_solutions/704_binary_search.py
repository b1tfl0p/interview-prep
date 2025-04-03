class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # avoid `(l + r) // 2` as it can lead to overflow
            mid = left + ((right - left) // 2)
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1
