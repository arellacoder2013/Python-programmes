#To find factors of user input
#Goes from 1 number and checks if i divides the number. If yes it is a factor
def print_factors(number):
    print("The factors of",number,"are:")
    for i in range (1, number + 1):
        if number % i ==0:
            print(i)
#Take input from user
number = int(input("Enter your number to find out the factors of the number :"))

#Calling our function
print_factors(number)

