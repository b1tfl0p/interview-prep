package solutions

import . "interview-prep/go-solutions/helpers"

func InvertTreeIter(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	arr := []*TreeNode{root}

	for len(arr) > 0 {
		top := arr[len(arr)-1]
		arr = arr[:len(arr)-1]
		top.Left, top.Right = top.Right, top.Left
		if top.Left != nil {
			arr = append(arr, top.Left)
		}
		if top.Right != nil {
			arr = append(arr, top.Right)
		}
	}

	return root
}
