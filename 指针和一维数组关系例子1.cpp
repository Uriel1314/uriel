#include<stdio.h>
int main(void)
{
	int x[10]={10,20,30,40,50,60,70,80,90,100};
	int *px,i;
	px=x;
//	printf("x=%d\n",*px);
	//traverse the array of x
	for(i=0;i<10;++i)
	{
		printf("%-4d",*px);
		px++;
	}
	printf("\n");
	//show sum
	px=x;
	int sum=0;
	for(i=0;i<10;++i)
	{
		sum=sum + *px;
		px++;
	}
	printf("sum=%d\n",sum);
	//show max
	px=x;
	int max=*px;
	for(i=0;i<10;++i)
	{
		if(max<*px)
			max=*px;
		px++;
	}
	printf("Max=%d\n",max);
	//show min
	px=x;
	int min=*px;
	for(i=0;i<10;++i)
	{
		if(min>*px)
			min=*px;
		px++;
	}
	printf("Min=%d\n",min);

	//show average
	int len=sizeof(x)/sizeof(*x);
	float average=(float)sum/len;
	printf("Average=%.2f\n",average);
	return 0;
}



