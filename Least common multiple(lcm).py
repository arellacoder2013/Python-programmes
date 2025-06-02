import math

def find_lcm(x, y):
    return abs(x*y) // math.gcd(x, y)

#Get input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Calculate and print the LCM
print("LCM:",find_lcm(num1,num2))