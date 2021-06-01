#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<malloc.h>

typedef struct Node
{
	int data;//数据域
	struct Node* pNext;//指针域
}NODE, * PNODE;//NODE等价于struct Node    PNODE等价于struct Node *

//函数声明
PNODE creat_list(void);
void traverse_list(PNODE pHead);
bool is_empty(PNODE pHead);
bool insert_list(PNODE pHead, int pos, int val);
int length_list(PNODE pHead);
bool delete_list(PNODE pHead, int pos, int* pVal);
void sort_list(PNODE pHead);

int main(void)
{
	PNODE pHead = NULL;//等价于 struct Node * pHead = NULL;

	pHead = creat_list();//create_list()功能：创建一个非循环单链表，并将该链表的头结点的地址付给pHead
	traverse_list(pHead);
	insert_list(pHead, 4, 33);
	traverse_list(pHead);
	if(is_empty(pHead))
	{
		printf("The Linked list is empty.\n");
	}
	else
	{
		printf("The Linked list is not empty.\n");
	}

	int len = length_list(pHead);
	printf("链表的长度是%d.\n", len);
	sort_list(pHead);
	traverse_list(pHead);

	return 0;
}

PNODE creat_list(void)
{
	int len, i, val;

	//分配了一个不存放有效数据的头结点
	PNODE pHead = (PNODE)malloc(sizeof(NODE));
	if (NULL == pHead)
	{
		printf("动态内存分配失败,程序终止.\n");
		exit(-1);
	}
	PNODE pTail = pHead;
	pTail->pNext = NULL;

	printf("请输入你想要生成的链表结点个数:");
	scanf_s("%d", &len);

	for (i = 0; i < len; ++i)
	{
		printf("请输入第%d个结点的值:", i + 1);
		scanf_s("%d", &val);

		PNODE pNew = (PNODE)malloc(sizeof(PNODE));
		if (pNew == NULL)
		{
			printf("动态内存分配失败,程序终止.\n");
			exit(-1);
		}
		pNew->data = val;
		pTail->pNext = pNew;
		pNew->pNext = NULL;
		pTail = pNew;

	}
	return pHead;
}

void traverse_list(PNODE pHead)
{
	PNODE p = pHead->pNext;

	while (NULL != p)
	{
		printf("%d  ", p->data);
		p = p->pNext;
	}
	printf("\n");

	return;
}

bool is_empty(PNODE pHead)
{
	if (NULL == pHead->pNext)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int length_list(PNODE pHead)
{
	PNODE p = pHead->pNext;
	int len = 0;

	while (p != NULL)
	{
		len++;
		p = p->pNext;
	}

	return len;
}

void sort_list(PNODE pHead)
{
	int i, j, t, len= length_list(pHead);
	PNODE p, q;

	for (i = 0, p = pHead->pNext; i < len - 1; ++i, p = p->pNext)
	{
		for (j = i + 1, q = p->pNext; j < len; ++j, q = q->pNext)
		{
			if (p->data > q->data)
			{
				t = p->data;
				p->data = q->data;
				q->data = t;
			}
		}
	}
	return;
}

bool insert_list(PNODE pHead, int pos, int val)
{
	int i = 0;
	PNODE p = pHead;

	while (NULL != p && i < pos - 1)
	{
		p = p->pNext;
		++i;
	}

	if (i > pos - 1 || NULL == p)
	{
		return false;
	}
	PNODE pNew = (PNODE)malloc(sizeof(NODE));
	if (NULL == pNew)
	{
		printf("动态内存分配失败!\n");
		exit(-1);
	}
	pNew->data = val;
	PNODE q = p->pNext;
	p->pNext = pNew;
	pNew->pNext = q;

	return true;
}