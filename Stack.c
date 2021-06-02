#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
#include<stdbool.h>

typedef struct NODE
{
	int data;//数据域
	struct NODE* pNext;//指针域
}NODE,*PNODE;

typedef struct Stack
{
	PNODE pTop;
	PNODE pBottom;
}STACK,*PSTACK;

//函数声明
void init(PSTACK pS);
void push(PSTACK pS, int val);
void traverse(PSTACK pS);
bool pop(PSTACK pS,int* pVal);
bool empt(PSTACK pS);
void clear(PSTACK pS);

int main(void)
{
	STACK S;//STACK<=>struct Stack
	int val;

	init(&S);
	push(&S, 1);
	push(&S, 2);
	push(&S, 3);
	push(&S, 4);
	push(&S, 5);
	printf("出栈前:\n");
	traverse(&S);
	if (pop(&S, &val))
	{
		printf("出栈成功,出栈元素为%d \n", val);
	}
	else
	{
		printf("出栈失败!\n");
	}
	printf("清空前:\n");
	traverse(&S);
	clear(&S);
	printf("清空后:\n");
	traverse(&S);

	return 0;
}

void init(PSTACK pS)
{
	pS->pTop = (PNODE)malloc(sizeof(NODE));
	if (pS->pTop == NULL)
	{
		printf("动态内存分配失败.\n");
		exit(-1);
	}
	else
	{
		pS->pBottom = pS->pTop;
		pS->pTop->pNext = NULL;//pS->pBottom->pNext==NULL
	}
}

void push(PSTACK pS, int val)
{
	PNODE pNew = (PNODE)malloc(sizeof(NODE));
	pNew->data = val;
	pNew->pNext = pS->pTop;//pS->pTop不能改成pS->pBottom
	pS->pTop = pNew;

	return;
}

void traverse(PSTACK pS)
{
	PNODE p = pS->pTop;
	while (p != pS->pBottom)
	{
		printf("%d  ", p->data);
		p = p->pNext;
	}
	printf("\n");

	return;
}

bool empt(PSTACK pS)
{
	if (pS->pTop == pS->pBottom)
		return true;
	else
		return false;
}

bool pop(PSTACK pS, int* pVal)
{
	if (empt(pS))//pS本身就是存放S的地址
	{
		return false;
	}
	else
	{
		PNODE r = pS->pTop;
		*pVal = r->data;
		pS->pTop = r->pNext;
		free(r);
		r = NULL;

		return true;
	}
}

void clear(PSTACK pS)
{
	if (empt(pS))
	{
		return;
	}
	else
	{
		PNODE p = pS->pTop;
		PNODE q = p->pNext;

		while (p!=pS->pBottom)
		{
			q = p->pNext;
			free(p);
			p = q;
		}
		pS->pTop = pS->pBottom;
	}
}
