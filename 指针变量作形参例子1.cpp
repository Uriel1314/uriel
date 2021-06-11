#include"stdio.h"

void fun(int x)
{
	x=x*10;
}

void fun2(int *p)
{
	*p=*p*10;
}
//数组作形参等价于指针作形参
int maxn(int *x,int n)
{
	int i,m;
	m=x[0];
	for(i=0;i<n;i++)
	{
		if(m<x[i])
			m=x[i];
	}
	return m;
}

int sumn(int *p,int n)
{
	int m=0,i;
	for(i=0;i<n;i++)
		m=m+p[i];
	return m;
}
void main()
{
	int a[5]={14,25,1,98,76},m;
	int *pa;
	m=maxn(a,5);
	printf("m=%d\n",m);
	pa=a;
	printf("%d\n",pa[4]);

	m=sumn(a,5);
	printf("%d\n",m);

}