#include"stdio.h"

//һά�ַ��������β�

int mystrlen(char s[])
{//���ַ����ĳ��� "abc"
	int len=0,i=0;		
	while(s[i]!='\0')
	{
		len++;
		i++;		
	}
	return len;
}
int digtotal(char s[])
{
	int count=0,i=0;
	while(s[i]!='\0')
	{
		if(s[i]>='0'&&s[i]<='9')
			count++;

		i++;
	}
	return count;
}
void main()
{
	char str[30]="zhang1233 san456";
	int x;
	x=mystrlen(str);
	printf("x=%d\n",x);
	x=digtotal(str);
	printf("x=%d\n",x);
}