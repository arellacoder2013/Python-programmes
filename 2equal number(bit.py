#program to check if user nput numbers are equal without using any  comparison
def  checkIfSame(number1,number2):
#using XOR operator as a^a is always  0
  if((number1 ^ number2)!= 0):
    print("numbers are not equal")
  else:
    print("both numbers are equal")
#taking input
number1 = int(input("Enter first number to compare :"))
number2 = int(input("Enter the second number to compare :"))

checkIfSame(number1, number2)