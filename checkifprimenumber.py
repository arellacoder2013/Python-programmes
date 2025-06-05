from math import sqrt

number = int(input("Enter your number"))
print("\n")

#If number is greater than 1
if number > 1:
    #check if number is divisible from 2 yo number/2
    for i in range(2,int(sqrt(number)+1)):
        if (number % i)==0:
            print(number,"Is not a prime number")
            break
    else:
        print(number,"is a prime number")
else:
     print(number,"is not prime number")
    #run the program