// 153. Find Minimum in Rotated Sorted Array

object Solution {
    def findMin(nums: Array[Int]): Int = {
        if (nums.size == 1 || nums(0) < nums(nums.size-1)) nums(0)
        else if (nums.size == 2) nums(1)
        else {
            if (nums(0) < nums(nums.size/2))
                findMin(nums.drop(nums.size/2))
            else
                findMin(nums.take(nums.size/2 + 1))
        }
    }
}
