#include"stdio.h"
/*
回顾：指针变量作形参
新内容：返回地址的函数（返回指针的函数）
*/

int *pfun(int *px,int *py)
{
	if(*px>*py)
		return px;
	else
		return py;

}
//返回较小数的地址？


int *pmaxn(int x[],int n)
{
	int i,max;
	int *pm;
	max=x[0];
	pm=&x[0];
	for(i=0;i<n;i++)
	{
		if(max<x[i])
		{
			max=x[i];
			pm=&x[i];
		}
	}
	return pm;
}
//返回n个数中最小数的地址?

void main()
{
	int x=10,y=20,*pmax;
	int a[5]={18,2,85,41,7};
	pmax=pfun(&x,&y);
	printf("%d\n",*pmax);

	pmax=pmaxn(a,5);
	printf("%d\n",*pmax);
}