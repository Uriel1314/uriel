#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<malloc.h>

typedef struct Node
{
	int data;//������
	struct Node* pNext;//ָ����
}NODE, * PNODE;//NODE�ȼ���struct Node    PNODE�ȼ���struct Node *

//��������
PNODE creat_list(void);
void traverse_list(PNODE pHead);
bool is_empty(PNODE pHead);
bool insert_list(PNODE pHead, int pos, int val);
int length_list(PNODE pHead);
bool delete_list(PNODE pHead, int pos, int* pVal);
void sort_list(PNODE pHead);

int main(void)
{
	PNODE pHead = NULL;//�ȼ��� struct Node * pHead = NULL;

	pHead = creat_list();//create_list()���ܣ�����һ����ѭ�������������������ͷ���ĵ�ַ����pHead
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
	printf("����ĳ�����%d.\n", len);
	sort_list(pHead);
	traverse_list(pHead);

	return 0;
}

PNODE creat_list(void)
{
	int len, i, val;

	//������һ���������Ч���ݵ�ͷ���
	PNODE pHead = (PNODE)malloc(sizeof(NODE));
	if (NULL == pHead)
	{
		printf("��̬�ڴ����ʧ��,������ֹ.\n");
		exit(-1);
	}
	PNODE pTail = pHead;
	pTail->pNext = NULL;

	printf("����������Ҫ���ɵ����������:");
	scanf_s("%d", &len);

	for (i = 0; i < len; ++i)
	{
		printf("�������%d������ֵ:", i + 1);
		scanf_s("%d", &val);

		PNODE pNew = (PNODE)malloc(sizeof(PNODE));
		if (pNew == NULL)
		{
			printf("��̬�ڴ����ʧ��,������ֹ.\n");
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
		printf("��̬�ڴ����ʧ��!\n");
		exit(-1);
	}
	pNew->data = val;
	PNODE q = p->pNext;
	p->pNext = pNew;
	pNew->pNext = q;

	return true;
}