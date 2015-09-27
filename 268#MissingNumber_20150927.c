// assume tha the array is already sorted acsendingly
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

