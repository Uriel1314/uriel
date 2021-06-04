#include"stdio.h"

void main()
{
	int a[3][3]={1,1,1,2,2,2,3,3,3},b[3][3]={10,10,10,20,20,20,30,30,30},c[3][3];
	int m[3][4]={1,8,104,5,10,54,3,69,97,1,0,8};
	int max,maxr,maxc,min,minr,minc;
	int i,j;
	printf("a:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%-4d",a[i][j]);
		}
		printf("\n");
	}

	printf("b:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%-4d",b[i][j]);
		}
		printf("\n");
	}

	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			c[i][j]=a[i][j]+b[i][j];
		}		
	}
	printf("c:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%-4d",c[i][j]);
		}
		printf("\n");
	}
	//求二维数组中的最大元素和最大元素的行号和列号
	max=m[0][0];
	maxr=0;
	maxc=0;
	for(i=0;i<3;i++)
	{
		for(j=0;j<4;j++)
		{
			if(max<m[i][j])
			{
				max=m[i][j];
				maxr=i;
				maxc=j;
			}
		}
	}
	printf("max=%d maxr=%d maxc=%d\n",max,maxr,maxc);
	//求二维数组中的最小元素和最小元素的行号和列号....
}