#include<stdio.h>
void main()
{
int x[10],i,j,temp,n;
printf("enter the number");
scanf("%d",&n);
printf("enter the number");
for(i=0;i<n;i++)
{
scanf("%d",&x[i]);
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(x[i]>x[j])
{
temp=x[i];
x[i]=x[j];
x[j]=temp;
}
}
}
for(i=0;i<n;i++)
{
printf("%d",x[i]);
}
}
