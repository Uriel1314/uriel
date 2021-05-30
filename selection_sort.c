-----------------------1------------------------ 
#include<stdio.h>
 void main()
 {
     int temp;
     int arr[5]={2,5,3,4,1};
    for(int i=0; i<5; i++) // 总共要找5-1次最大值,每次找最大值的区间 [0,5-i]
    {
         int index_max = 0;
        for(int j=1; j<5-i; j++) // 因为假设了0下标就是最大值，所以循环可以从1开始
        {
            if(arr[j] > arr[index_max])
            {
                index_max = j;
            }
        }        
        if(index_max != 5-i-1) // 避免无意义的位置交换
        {
            int temp = arr[index_max];
            arr[index_max] = arr[5-i-1];
            arr[5-i-1] = temp;
        }
    }
    //打印排序后输出的结果
    for (int i = 0; i < 5; ++i)
    {
    printf("%d  ",arr[i]);
    }
    printf("\n");
 }

----------------------2-------------------------
#include<stdio.h>
void main()
{
    int i,j,temp;
    int arr[5]={5,4,7,6,1};
 
    for (i = 0 ; i < 5 - 1 ; i++) 
    {
        int min = i;                  // 记录最小值，第一个元素默认最小
        for (j = i + 1; j < 5; j++)     // 访问未排序的元素
        {
            if (arr[j] < arr[min])    // 找到目前最小值
            {
                min = j;    // 记录最小值
            }
        }
        if(min != i)
        {
            temp=arr[min];  // 交换两个变量
            arr[min]=arr[i];
            arr[i]=temp;
        }
    }
    //打印输出的结果
    for (int i = 0; i < 5; ++i)
    {
    printf("%d  ",arr[i]);
    }
    printf("\n");
}

-------------------3------------------------
 #include<stdio.h>
 void main()
 {
     int temp;
     int arr[5]={2,5,3,4,1};
    for(int i=0; i<5; i++) // 总共要找5-1次最大值,每次找最大值的区间 [0,5-i]
    {
         int index_max = 0;
        for(int j=1; j<5-i; j++) // 因为假设了0下标就是最大值，所以循环可以从1开始
        {
            if(arr[j] > arr[index_max])
            {
                index_max = j;
            }
        }        
        if(index_max != 5-i-1) // 避免无意义的位置交换
        {
            int temp = arr[index_max];
            arr[index_max] = arr[5-i-1];
            arr[5-i-1] = temp;
        }
    }
    //打印排序后输出的结果
    for (int i = 0; i < 5; ++i)
    {
    printf("%d  ",arr[i]);
    }
    printf("\n");
 }