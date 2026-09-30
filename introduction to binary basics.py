n=int(input("Enter a number (try 5 or 12)"))
guess = input("Guess its binary: ")

input("Binary. Press enter")
print(" decimal",n,"->binary",bin(n)[:2])
print(" your guess:",guess)

#AND=both bits must be 1
input("AND=both bits must be 1.Press enter")
print("12=",bin(12[:2]))
print("10=",bin(10[:2]))
print("12&10=",12 & 10)

#OR ~ at least one bit is 1
input("OR ~ at least one bit is one.Press enter")
print("12 | 10=",12|10)
