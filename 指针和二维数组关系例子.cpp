#include"stdio.h"
//int maxn3(int x[][3],int n)
int maxn3(int (*x)[3],int n)
{//行指针变量作形参等价于二维数组作形参
	int i,j,m;
	m=x[0][0];
	for(i=0;i<n;i++)
	{
		for(j=0;j<3;j++)
		{
			if(m<x[i][j])
				m=x[i][j];
		}
	}
	return m;
}

void main()
{
	int a[3][3]={10,20,30,440,50,60,70,80,90},*pa,i;	
	//行指针变量
	int (*pr)[3];
	//可以使用指针变量引用二维数组任意元素
	pa=&a[0][0];	
	printf("%d\n",a[0][0]);
	printf("%d\n",*pa);
	//
	for(i=0;i<9;i++)
	{
		printf("%-4d",*pa);
		pa++;
	}
	printf("\n");
	//a[i][j]地址表示方式：（1）&a[i][j];(2)a[i]+j;(3)*(a+i)+j;
	pa=a[0]+2;
	printf("%d\n",*pa);
	pa=*(a+0)+2;
	printf("%d\n",*pa);
	//行指针变量应用
	pr=a+2;
	printf("%d\n",pr[0][2]);
	//
	printf("%d\n",maxn3(a,3));
	//
	printf("===%d\n",a[1][0]);
	printf("===%d\n",*(&a[1][0]));
	printf("===%d\n",*(a[1]+0));
	printf("===%d\n",*(*(a+1)+0));
}