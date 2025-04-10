package solutions

import (
	"slices"
	"testing"
)

func TestBuildTree(t *testing.T) {
	preorder := []int{1, 2, 3, 4}
	inorder := []int{2, 1, 3, 4}
	answer := []int{1, 2, 3, 0, 0, 0, 4}

	got := BuildTree(preorder, inorder)
	gotSlice := got.ToIntSlice()
	if !slices.Equal(gotSlice, answer) {
		t.Errorf(
			"buildTree(%v, %v) == %+v, want %v",
			preorder,
			inorder,
			gotSlice,
			answer,
		)
	}
}
