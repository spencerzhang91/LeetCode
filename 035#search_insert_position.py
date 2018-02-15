#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 35 Search Insert Position
"""
Created on Thu Feb 15 10:20:47 2018

@author: spencer
"""
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high + low) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return low

        
if __name__ == "__main__":
    
    sol = Solution()
    assert sol.searchInsert([1,3,5,6], 5) == 2
    assert sol.searchInsert([1,3,5,6], 2) == 1
    assert sol.searchInsert([1,3,5,6], 7) == 4
    assert sol.searchInsert([1,3,5,6], 0) == 0
    assert sol.searchInsert([1,2,3,4,5,6,9], 0) == 0
    assert sol.searchInsert([0,3,5], 90) == 3
    assert sol.searchInsert([1,3,5], 3) == 1
    assert sol.searchInsert([1,3,5,7], 3) == 1
    assert sol.searchInsert([0,1,3,5], 3) == 2
    assert sol.searchInsert([0], 0) == 0
    assert sol.searchInsert([1,2], 1) == 0
    assert sol.searchInsert([1,2], 2) == 1
    assert sol.searchInsert([1,2], 3) == 2
    assert sol.searchInsert([1,2], 0) == 0
    assert sol.searchInsert([2], 0) == 0
    assert sol.searchInsert([2], 3) == 1
    assert sol.searchInsert([2], 2) == 0
    assert sol.searchInsert([1,3], 2) == 1
