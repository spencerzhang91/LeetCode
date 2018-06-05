// 836. Rectangle Overlap
package main

func isRectangleOverlap(rec1 []int, rec2 []int) bool {
	// Let's set rec1 to be the base rectangle.
	// It's implied that upper left -- bottom right relationship has certain
	// implicit bounding on location of the two anchor point.
	if rec1[0] >= rec2[0] && rec1[1] >= rec2[1] && rec1[0] < rec2[2] && rec1[1] < rec2[3] {
		return true
	} else if rec1[0] >= rec2[2] || rec1[1] >= rec2[3] {
		return false
	} else if rec1[0] <= rec2[0] && rec1[1] >= rec2[1] {
		if rec1[2] > rec2[0] {
			return true
		}
		return false
	} else if rec1[0] <= rec2[0] && rec1[1] <= rec2[1] {
		if rec1[2] > rec2[0] && rec1[3] > rec2[1] {
			return true
		}
		return false
	} else if rec1[0] >= rec2[0] && rec1[1] <= rec2[1] {
		if rec1[3] > rec2[1] {
			return true
		}
		return false
	}
	return false
}
