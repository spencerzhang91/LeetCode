// assume that the array is already sorted acsendingly
int missingNumber(int* nums, int numsSize)
{
	int mid;
	int left = 0;
    int right = numsSize;
    mid = (left + right) / 2;
    while (left < right)
    {
    	if (nums[mid] > mid)
	    	right = mid;
	    else
	    	left = mid + 1;
	    mid = (left + right) / 2;
	}
	return left;
}

// not assuming sorted approach below:
int missingNumber(int *nums, int numsSize)
{
    int temp = numsSize;
    for (int i = 0; i < numsSize; i++)
    {
        temp ^= nums[i];
        temp ^= i;
    }
    
    return temp;
}
