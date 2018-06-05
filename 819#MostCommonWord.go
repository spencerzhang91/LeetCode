// 819. Most Common Word
package main

import "strings"

func uniqueList(slist []string) []string {
	unique := make([]string, 0)
	for _, w := range slist {
		if isInside(unique, w) {
			continue
		} else {
			unique = append(unique, w)
		}
	}
	return unique
}

func isInside(slice []string, word string) bool {
	for _, w := range slice {
		if w == word {
			return true
		}
	}
	return false
}

// Count helper function
func Count(slice []string, target string) int {
	count := 0
	for _, word := range slice {
		if word == target {
			count++
		}
	}
	return count
}

func mostCommonWord(paragraph string, banned []string) string {
	paragraph = strings.ToLower(paragraph)
	for _, p := range []string{"!", "?", "'", ";", ".", ","} {
		paragraph = strings.Replace(paragraph, p, "", -1)
	}
	ls := strings.Split(paragraph, " ")
	words := uniqueList(ls)
	var res string
	count := 0
	for _, word := range words {
		if !isInside(banned, word) {
			temp := Count(ls, word)
			if temp > count {
				res = word
				count = temp
			}
		}
	}
	return res

}
