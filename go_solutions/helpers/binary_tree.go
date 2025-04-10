package helpers

import "container/list"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func (t *TreeNode) ToIntSlice() []int {
	nodes := make([]int, 0)
	if t == nil {
		return nodes
	}

	q := list.New()
	q.PushBack(t)

	zeroCount := 0
	for q.Len() > 0 {
		n := q.Remove(q.Front()).(*TreeNode)
		if n == nil {
			zeroCount++
			continue
		}

		if zeroCount > 0 {
			nodes = append(nodes, make([]int, zeroCount)...)
			zeroCount = 0
		}
		nodes = append(nodes, n.Val)

		q.PushBack(n.Left)
		q.PushBack(n.Right)
	}

	return nodes
}

func NewTree(nodes []int) *TreeNode {
	if len(nodes) == 0 || nodes[0] == -1 {
		return nil
	}

	root := &TreeNode{Val: nodes[0]}
	if len(nodes) == 1 {
		return root
	}

	q := make([]*TreeNode, len(nodes)/2)
	q = append(q, root)
	for i := 0; i < len(nodes); i += 3 {
		n := q[i]
		n.Left = &TreeNode{Val: nodes[i+1]}
		n.Right = &TreeNode{Val: nodes[i+2]}
		q = append(q, n.Left, n.Right)
	}
	return root
}
