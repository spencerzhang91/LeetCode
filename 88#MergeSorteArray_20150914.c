/* 88 Merge Sorted Array */
#include <stdio.h>
#define M 7
#define N 6
void merge(int *nums1, int m, int *nums2, int n);
int main(void)
{
	int nums1[M+N+1] = {1,2,3,5,7,9,11};
	int nums2[N] = {4,5,6,8,12,15};
	merge(nums1, M, nums2, N);
	
	for (int i = 0; i < M+N+1; i++)
		printf("%d ", nums1[i]);
	
	return 0;
}

void merge(int *nums1, int m, int *nums2, int n)
{
	
	return;
}








