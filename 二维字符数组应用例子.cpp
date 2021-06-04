#include"stdio.h"

void main()
{
	//char name[5][30]={"zhang san","li si","wang wu","abc","abd"};
	char name[5][30];
	int i;
	printf("input 5 string:\n");
	i=0;
	while(i<5)
	{
		//scanf("%s",name[i]);
		gets(name[i]);
		i++;
	}

	printf("name:\n");
	for(i=0;i<5;i++)
	{
		//printf("%s\n",name[i]);
		puts(name[i]);
	}

	printf("\n");

}