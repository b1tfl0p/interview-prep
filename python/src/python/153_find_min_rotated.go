package binary_search

func findMin(nums []int) int {
	var (
		l = 0
		r = len(nums)
		m int
	)
	for l < r {
		m = l + (r-1)/2
		if nums[l] < nums[r] {
			r = m
		} else {
			l = m + 1
		}
	}
	return nums[l]
}
