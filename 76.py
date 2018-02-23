a = input()
if a > 1:
   for i in range(2,a):
       if (a % i) == 0:
           print("is composite number number")
           break
   else:
       print("is a prime number")
else:
   print("is composite number")
