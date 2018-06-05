// 817. Linked List Components
package main

import "fmt"

// ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func makeLinkeList(list []int) *ListNode {
	head := &(ListNode{Val: list[0], Next: nil})
	curr := head
	for _, val := range list[1:] {
		newNode := &(ListNode{Val: val, Next: nil})
		(*curr).Next = newNode
		curr = (*curr).Next
	}
	return head
}

func printLinkedList(head *ListNode) {
	for head != nil {
		fmt.Printf("%d ", (*head).Val)
		head = head.Next
	}
}

func set(list []int) map[int]int {
	mapset := make(map[int]int)
	for k, v := range list {
		mapset[v] = k // this is a trick caused by golang
	}
	return mapset
}

func numComponents(head *ListNode, G []int) int {
	Gset := set(G)
	curr := head
	prev := false
	count := 0
	for curr != nil {
		_, ok := Gset[(*curr).Val]
		if ok && !prev {
			count++
		}
		prev = ok
		curr = (*curr).Next
	}
	return count
}
