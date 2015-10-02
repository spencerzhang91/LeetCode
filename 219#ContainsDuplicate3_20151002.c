/* #219 contains duplicate2 */
/* basic slow unacceptable O(n^2) approach */

bool containsNearbyDuplicate(int *nums, int numsSize, int k)
{
	for (int i = 0; i < numsSize; i++)
		for (int j = i+1; j < i+k+1; j++)
			if (nums[i] == nums[j])
				return true;
				
	return false;
} 
