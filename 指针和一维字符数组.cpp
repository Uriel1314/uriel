#include"stdio.h"
void main()
{//ָ�������һά�ַ����飨�ַ�������ϵ
	char s[10]="abc123de2",*ps;
	int len=0,count=0;
	ps=&s[0];//ps=s;
	printf("%c\n",*ps);
	puts(s);
	puts(ps);
	//ps++;
	//printf("%c\n",*ps);
	//puts(ps);
	while(*ps!='\0')
	{
		len++;
		ps++;
	}
	printf("len=%d\n",len);
	ps=s;
	while(*ps!='\0')
	{
		if(*ps>='0'&&*ps<='9')
			count++;
		ps++;
	}
	printf("count=%d\n",count);
	ps=s;
	while(*ps!='\0')
	{
		if(*ps>='a'&&*ps<='z')
			*ps=*ps-32;
		ps++;
	}
	puts(s);


}