#include"stdio.h"
//int maxn3(int x[][3],int n)
int maxn3(int (*x)[3],int n)
{//��ָ��������βεȼ��ڶ�ά�������β�
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
	//��ָ�����
	int (*pr)[3];
	//����ʹ��ָ��������ö�ά��������Ԫ��
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
	//a[i][j]��ַ��ʾ��ʽ����1��&a[i][j];(2)a[i]+j;(3)*(a+i)+j;
	pa=a[0]+2;
	printf("%d\n",*pa);
	pa=*(a+0)+2;
	printf("%d\n",*pa);
	//��ָ�����Ӧ��
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