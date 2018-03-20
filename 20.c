# include <stdio.h> 
# include <conio.h>
void main() 
{ 
 int x,y,div ; 
 clrscr() ; 
 printf("Enter the limit : ") ; 
 scanf("%d", &y) ; 
 printf("\nEnter the number : ") ; 
 scanf("%d", &div) ; 
 printf("\nThe numbers divisible by %d are :\n\n", div) ; 
 for(x = 1 ; x <= y ; x++) 
  if(x % div == 0) 
   printf("%d\t", x) ; 
 getch() ; 
}
