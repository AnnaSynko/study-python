#Факторіал числа
import math

number = int(input("Enter num = ")) 
fact = 1
while(number > 1):
    fact *= number
    number -= 1
    
print(fact)

#Second method
n = 5
print("N = ", math.factorial(n))