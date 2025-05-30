#Program to  find HCF/GCD
#Enter 2 numbers

number_largest = int(input("Enter Largest number:"))
number_smallest= int(input("Enter Smallest number:"))

#Using Eucliden Algorithms
while(number_smallest):
    number_Store = number_smallest
    number_smallest = number_largest % number_smallest
    number_largest = number_Store

print("HCF is :",number_largest)
