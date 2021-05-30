#include"stdio.h"

/*int sum2(int x,int y)
{
	int z;
	z=x+y;
	return z;
}

void fun(int x)
{
	x=x*10;
}
*/

//普通变量作形参，从实参到形参是值单向传递方式
//...
//数组作形参
/*
int max10(int x[10])
{
	int m,i;
	m=x[0];
	for(i=0;i<10;i++)
	{
		if(m<x[i])
			m=x[i];
	}
	return m;
}
*/
int maxn(int x[],int n)
{
	int m,i;
	m=x[0];
	for(i=0;i<n;i++)
	{
		if(m<x[i])
			m=x[i];
	}
	return m;
}

//int minn(int x[],int n){}
int minn(int x[], int n)
{
	int i,m;
	m=x[0];
	for(i=0;i<n;++i)
	{
		if(m>x[i])
		{
			m=x[i];
		}
	}
	return m;
}

int sumn(int x[],int n)
{
	int sum=0,i;
	for(i=0;i<n;i++)
		sum+=x[i];
	return sum;
}
//float aven(int x[],int n){ }
void bubblesort(int x[],int n)
{
	for(int i = 0;i<n-1;++i)
	{
		for(int j=0;j<n-1-i;++j)
		{
			if(x[j]>x[j+1])
			{
				int t=x[j];
				x[j]=x[j+1];
				x[j+1]=t;
			}
		}
	}
}
//void selectsort(int x[],int n){}
void fun2(int x[],int n)
{
	int i;
	for(i=0;i<n;i++)
		x[i]=x[i]*10;
}

void traverse(int s[],int n)
{
	int i;
	for(i=0;i<5;i++)
		printf("%-4d",s[i]);
	printf("\n");
}

void selection_sort(int arr[], int n)
{
	int i,j,temp;
	for(i=0;i<n-1;++i)
	{
		int min=i;
		for(j=i+1;j<n;++j)
		{
			if(arr[j]<min)
				min=arr[j];
		}
		if(min!=i)
		{
			temp=arr[min];
			arr[min]=arr[i];
			arr[i]=temp;
		}
	}
}
void main()
{
	/*普通变量作形参
	int x=11,y=12,z;
	int a=5;
	z=sum2(x,y);
	printf("%d\n",z);
	fun(a);
	printf("a=%d\n",a);
	*/
	//数组作形参实验
	int arr[10]={12,1,58,36,4787,1,2,3,9,780};
	int s[5]={87,48,21,98,0};
	int m,i;
	//show max
	m=maxn(arr,10);
	printf("m=%d\n",m);
	//show max of s[5]
	m=maxn(s,5);
	printf("m=%d\n",m);
	//show sum of s[]
	m=sumn(s,5);
	printf("m=%d\n",m);
	//show bubble_sortion
	printf("排序前---------------\n");
	traverse(s,5);
	bubblesort(s,5);
	printf("排序后---------------\n");
	traverse(s,5);
	//show 扩大十倍s[]
	fun2(s,5);
	traverse(s,5);
	//show min of s[]
	printf("min=%d\n",minn(s,5));



}