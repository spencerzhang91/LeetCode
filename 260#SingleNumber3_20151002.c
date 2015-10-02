#include <stdio.h>
#include <stdlib.h>
#define N 8

int *singleNumber(int *nums, int numsSize, int *returnSize);

int main(void)
{
	int array[N] = {1,2,3,4,4,5,3,2};
	int *result;
	int size = 2;
	result = singleNumber(array, N, &size);
	
	for (int i = 0; i < 2; i++)
		printf("%d ", result[i]);
	 
	return 0;
}

int *singleNumber(int *nums, int numsSize, int *returnSize)
{
	int temp = 0;
	*returnSize = 2;
	int *ret = (int *)malloc(2 * sizeof(int));
	ret[0] = 0; ret[1] = 0;

	for (int i = 0; i < numsSize; i++)
		temp ^= nums[i];
		
	temp &= -temp;
	for (int j = 0; j < numsSize; j++)
	{
		if ((nums[j] & temp) == 0)
			ret[0] ^= nums[j];
		else
			ret[1] ^= nums[j];				
	}
	
	return ret;
}
