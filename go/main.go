package main

import (
	"fmt"

	"github.com/b1tfl0p/interview-prep/go/solutions"
)

func main() {
	preorder := []int{1, 2, 3, 4}
	inorder := []int{2, 1, 3, 4}
	answer := []int{1, 2, 3, 0, 0, 0, 4}

	got := solutions.BuildTree(preorder, inorder)
	gotSlice := got.ToIntSlice()
	fmt.Printf(
		"buildTree(%v, %v) == %+v, want %v",
		preorder,
		inorder,
		gotSlice,
		answer,
	)
}
