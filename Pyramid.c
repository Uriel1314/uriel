#include <stdio.h>

void pyramid( int n );

int main()
{    
    int n;

    scanf("%d", &n);
    pyramid(n);

    return 0;
}

void pyramid( int n )
{
    int i,j;
    for(i=1;i<=n;++i)
    {
        for(j=1;j<=n+1-i;++j)
        {
            printf(" ");
        }
        for (j = 1; j <= i; j++)
    {
        printf("%d ", i);
    }
        printf("\n");
    }
}