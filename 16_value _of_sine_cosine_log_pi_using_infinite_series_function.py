""" Design a Python Script to find the value of (Sine, Cosine, Log, PI, e) of a given number using infinite series of the function. """
import math
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine
print(round(sin(x,n),2))

import math
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
def cosine(x,n):
    cosx = 1
    sign = -1
    for i in range(2, n, 2):
        pi=22/7
        y=x*(pi/180)
        cosx = cosx + (sign*(y**i))/math.factorial(i)
        sign = -sign
    return cosx
print(round(cosine(x,n),2))

list_ex = []
list_ex.append(1)
for i in range(1,n):
    num_ex = i
    fact_ex = 1
    for j in range(i):
        fact_ex=fact_ex*num_ex
        num_ex-=1
    ans_ex = (x**(i))/fact_ex
    list_ex.append(ans_ex)
print(sum(list_ex))
