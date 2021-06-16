#include<stdio.h>
int *max(int* a, int len);
int* min(int* a, int len);
void selection_sort(int arr[], int len);
void swap(int* a, int* b);
void traverse(int* a, int len);
void swap2(int* a, int* b);
void swap3(int *a, int *b);

int main(void)
{
	int arr[] = { 5,6,4,2,1,3,9,7,8,10 };
	int len = sizeof(arr) / sizeof(arr[0]);
	printf("Max=%d\n",*max(arr, len));
	printf("Min=%d\n", *min(arr, len));
	selection_sort(arr, len);
	traverse(arr, len);

	return 0;
}

int* max(int* a, int len)
{
	int i, * pArr;
	pArr = &a[0];
	for (i = 0; i < len; ++i)
	{
		if (*pArr < a[i])
		{
			pArr = &a[i];
		}
	}
	return pArr;
}

int* min(int* a, int len)
{
	int i, * pArr;
	pArr = &a[0];
	for (i = 0; i < len; ++i)
	{
		if (*pArr > a[i])
		{
			pArr = &a[i];
		}
	}
	return pArr;
}

void selection_sort(int arr[], int len)
{
	int i, j;
	for (i = 0; i < len-1; ++i)
	{
		int min = i;
		for (j = i+1; j < len; ++j)
		{
			if (arr[min] > arr[j])
			{
				min = j;//record the minimum
			}
		}
		swap(&arr[min], &arr[i]);
		//swap2(&arr[min], &arr[i]);
		//swap3(&arr[min], &arr[i]);
		

	}
}

void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

void traverse(int* a, int len)
{
	int i;
	for (i = 0; i < len; ++i)
	{
		printf("%-4d", a[i]);
	}
	printf("\n");
}

void swap2(int* a, int* b)
{
	*a ^= *b ^= *a ^= *b;
}

void swap3(int* a, int* b)
{
	*b = (__int64)((__int64)*a << 32 | (*a = *b)) >> 32;
}