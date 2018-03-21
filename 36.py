#include<stdio.h>
void main()
{
char str[50],x,c=0;
printf("enter the word");
gets(str);
for(x=0;str[x]!='\0';i++)
{
if((str[x]>='0')&&(str[x]<='9')||(str[x]>='a')&&(str[x]<='z'))
{
continue;
}
else
{
    c++;
}
}


printf("%d",c);
}
