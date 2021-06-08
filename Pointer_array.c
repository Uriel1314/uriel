#include<stdio.h>

//函数声明
void traverse(int arr[], int len);
void selection_sort(int arr[],int len);
void swap(int* a, int* b);
int Max_array(int arr[], int len);
int Min_array(int arr[], int len);
int sum_array(int arr[], int len);
float average(int arr[], int len);

int main(void)
{
	int arr[] = { 20,10,30,90,80,60,70,40,50,100 };
	int len = sizeof(arr) / sizeof(*arr);
	printf("排序前: ");
	traverse(arr, len);
	selection_sort(arr,len);
	printf("排序后: ");
	traverse(arr, len);
	printf("Min=%d\t\t", Min_array(arr,len));
	printf("Max=%d\n", Max_array(arr, len));
	printf("Sum=%d\t\t", sum_array(arr, len));
	printf("Average=%.2f\n", average(arr, len));

	return 0;
}

//遍历输出Array
void traverse(int arr[], int len)
{
	int i, j;
	for (i = 0; i < len; ++i)
	{
		printf("%-4d", arr[i]);
	}
	printf("\n");
	return;
}
//对数组进行排序
void selection_sort(int arr[],int len)
{
	int i, j;
	for (i = 0; i < len-1; ++i)
	{
		int min = i;
		for (j = i+1; j < len; ++j)
		{
			if (arr[j] < arr[min])
			{
				min = j;
			}
		}
		swap(&arr[min], &arr[i]);
	}
	return;
}
//交换两个变量
void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
	return;
}
//求最小值
int Min_array(int arr[], int len)
{
	int i;
	int min = arr[0];
	for (i = 0; i < len; ++i)
	{
		if (arr[i] < min)
		{
			min = arr[i];
		}
	}
	return min;
}
//求最大值
int Max_array(int arr[], int len)
{
	int i;
	int max = arr[0];
	for (i = 0; i < len; ++i)
	{
		if (arr[i] > max)
		{
			max = arr[i];
		}
	}
	return max;
}
//求和
int sum_array(int arr[],int len)
{
	int i, sum = 0;
	for (i = 0; i < len; ++i)
	{
		sum += arr[i];
	}
	return sum;
}
//求平均值
float average(int arr[], int len)
{
	return (float)(sum_array(arr, len) / len);//强制类型转换,把'int'转换为'float'
}