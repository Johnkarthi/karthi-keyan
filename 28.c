#include<stdio.h>
int main()
{
int Array[] = { 5, 8, 3, 7 };
int Element = 3;
int Index;

for (int i = 0; i < Array.Length; i++)
{
     if (Element == Array[i])
     {
         Index = i;
     }
}
printf("index:",Index);
return 0;
}
