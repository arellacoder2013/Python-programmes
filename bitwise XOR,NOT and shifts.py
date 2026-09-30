#XOR-different number s equal to one eg 1|0=1
#NOT-changes to opposite if number =1 not will make it 0
n=int(input("Enter a number(try 5 or 12)"))
guess=input("Left shift double sit .Guess: " + str(n) + "<< 1=?")


input("NOt-flips every bit .Press enter")
print(" 12=",bin(12)[2:])
print("NOT 12=",~12 & 0xFF)

input("XOR-different bits give 1.Press enter")
print("12 ^10=",12^10)

#Left shift -multiplies by 2
input("Left shift -multiplies by 2.Press enter")
print(" ",n, "<< 1=",n <<1," your guess:",guess)

#Right shift -divides by 2
input("Right shift -divides by 2.Press enter")
print(" ",n,">> 1 =",n>>1)