/* 88 Merge Sorted Array */
// long stupid insert approach:
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
		arr[i+1] = arr[i];
	arr[place] = num;
}

// and here comes the one line solution: 
void merge(int* nums1, int m, int* nums2, int n) {
    while(n)
        nums1[m+n-1] = (m && nums1[m-1] > nums2[n-1]) ? nums1[--m]:nums2[--n];
}

