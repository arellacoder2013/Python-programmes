#factorial using recursion

def factorial(n):
    if n==0:
        return 1#factorial of 0 is always 1
    return n * factorial(n-1)

input("Factorial -n! = n x(n-1) x ... x 1 base case: 0! =1.Press Enter")
print(" 6!=",factorial(6)," 6x5x4x3x2x1")
print(" 5!=",factorial(5)," 5x4x3x2x1")

n=int(input("Enter a number (try 4 or 8):"))
guess = input("What is"+str(n) +"!?")
input("n! = nx factorial(n-1) base case:0! =1.Press Enter")
print(" ",str(n)+ "!=",factorial(n),"your guess:",guess)

