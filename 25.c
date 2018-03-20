#include <stdio.h>
int main()
{
    int x[10];
    int n;
    int i, j, temp;
            scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&x[i]);
    }

    for(i=0;i<n;i++)
    {
            for(j=i;j<n;j++)
        {
                if(x[i]>x[j])
            {
                temp=x[i];
                x[i]=x[j];
                x[j] = temp;
            }
        }
    }
    printf("%d",a[n/2]);
    return 0;
}
