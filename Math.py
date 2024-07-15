import math
from math import factorial as fac
from math import sqrt as root
from math import pow as power

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

for i in range (5): #print the square root from 1 to 5 using for loop
    print (int(root(i))) #typecasting the float values to integer values

print (power(2,5)) #print 2 raised to the power 5

print ("Cosine of 2.5 is", math.cos(2.5)) #print cosine of 2.5

print ("sine of 2.5 is", math.sin(2.5)) #print sine of 2.5