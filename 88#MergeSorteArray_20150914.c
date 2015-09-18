/* 88 Merge Sorted Array */
#include <stdio.h>
#define M 10
#define N 0

void merge(int *nums1, int m, int *nums2, int n);
int binary_search(int num, int *arr, int len);
void insert_item(int num, int *arr, int len, int place);

int main(void)
{
	int nums1[M*2] = {1,2,3,5,7,9,11,18,20,30};
	int nums2[N] = {};
	
	printf("%d -> %d\n", 0, binary_search(0, nums1, M));
	printf("%d -> %d\n", 1, binary_search(1, nums1, M));
	printf("%d -> %d\n", 2, binary_search(2, nums1, M));
	
    printf("%d -> %d\n", 8, binary_search(8, nums1, M));
	printf("%d -> %d\n", 9, binary_search(9, nums1, M));
	printf("%d -> %d\n", 10, binary_search(10, nums1, M));
	printf("%d -> %d\n", 11, binary_search(11, nums1, M));
	printf("%d -> %d\n", 12, binary_search(12, nums1, M));
	printf("%d -> %d\n", 16, binary_search(16, nums1, M));
	printf("%d -> %d\n", 17, binary_search(17, nums1, M));
	
	printf("%d -> %d\n", 29, binary_search(29, nums1, M));
	printf("%d -> %d\n", 30, binary_search(30, nums1, M));
	printf("%d -> %d\n", 31, binary_search(31, nums1, M));
	
	merge(nums1, M, nums2, N);
	
	for (int i = 0; i < M*2; i++)
		printf("%d ", nums1[i]);
	
	return 0;
}

void merge(int *nums1, int m, int *nums2, int n)
{
	
    for (int i = 0; i < n; i++)
		insert_item(nums2[i], nums1, m*2, binary_search(nums2[i], nums1, m+i) + 1);
}

int binary_search(int num, int *arr, int len)
{
	int min = 0;
	int max = len - 1;
	while (min <= max)
	{
		if (num == arr[(min+max)/2])
			return (min + max) / 2;
			
		else if (num < arr[(min+max)/2])
			max = (min + max)/2 - 1;
			
		else if (num > arr[(min+max)/2])
			min = (min + max)/2 + 1;
	}
	return (min + max) / 2;
}

void insert_item(int num, int *arr, int len, int place)
{
	for (int i = len-1; i >= place; i--)
	{
		arr[i+1] = arr[i];
	}
	arr[place] = num;
}

