#include<stdio.h>
int main()
{
int A[] = { 5, 8, 3, 7 };
int E = 3;
int Index;

for (int i = 0; i < A.Length; i++)
{
     if (E == A[i])
     {
         Index = i;
     }
}
printf("index:",Index);
return 0;
}
