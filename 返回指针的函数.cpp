#include"stdio.h"
/*
�عˣ�ָ��������β�
�����ݣ����ص�ַ�ĺ���������ָ��ĺ�����
*/

int *pfun(int *px,int *py)
{
	if(*px>*py)
		return px;
	else
		return py;

}
//���ؽ�С���ĵ�ַ��


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
//����n��������С���ĵ�ַ?

void main()
{
	int x=10,y=20,*pmax;
	int a[5]={18,2,85,41,7};
	pmax=pfun(&x,&y);
	printf("%d\n",*pmax);

	pmax=pmaxn(a,5);
	printf("%d\n",*pmax);
}