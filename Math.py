import math
from math import factorial as fac

#printing factorial using dot operator for math library
print(math.factorial(5))

#using factorial as fac variable
n=100
k=2
#How many ways can we draw 2 apples from 100 apples

ways= fac(n)//(fac(k)*fac(n-k))

print ("You can draw",ways,"ways 2 apples from 100 apples")

print (fac(n)) #This gives us a big number

print(len(str(fac(n)))) #This will give us the number of digits in factorial n