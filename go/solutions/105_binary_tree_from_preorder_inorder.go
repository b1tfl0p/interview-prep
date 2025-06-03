package solutions

import "github.com/b1tfl0p/interview-prep/go/helpers"

func BuildTree(preorder []int, inorder []int) *helpers.TreeNode {
	inorderMap := make(map[int]int)
	for i, val := range inorder {
		inorderMap[val] = i
	}

	i := 0

	var dfs func(l, r int) *helpers.TreeNode
	dfs = func(l, r int) *helpers.TreeNode {
		if l > r {
			return nil
		}

		nodeVal := preorder[i]
		i++
		mid := inorderMap[nodeVal]
		node := &helpers.TreeNode{
			Val:   nodeVal,
			Left:  dfs(l, mid-1),
			Right: dfs(mid+1, r),
		}
		return node
	}

	return dfs(0, len(inorder)-1)
}
