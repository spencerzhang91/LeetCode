#include <stdio.h>
int maxSubArray(int *nums, int numsSize);

int main(void)
{
    int numArray[9] = {-2,1,-3,4,-1,2,1,-5,4};
    int max = maxSubArray(numArray, 9);

    printf("The max sum is %d.\n", max);
    return 0;
}

int maxSubArray(int* nums, int numsSize)
{
    int max_array[numsSize];
    max_array[numsSize-1] = nums[numsSize-1];
    int curr_max = max_array[numsSize-1];
    for (int j=2; j <= numsSize; j++)
    {
        if (max_array[numsSize-j+1] >= 0)
            max_array[numsSize-j] = nums[numsSize-j] + max_array[numsSize-j+1];
        else
            max_array[numsSize-j] = nums[numsSize-j];
        if (max_array[numsSize-j] > curr_max)
            curr_max = max_array[numsSize-j];
    }
    return curr_max;
}