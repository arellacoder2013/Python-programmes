#checking the power of 2
#set bits is 1,zero bit is 0

input("Set a bit-OR turns it on .Press enter")
print("5=",bin(5)[2:])
print("5|2=",5 |2,"binary:,bin(5|2)[2:]")

input("Zero a bit -AND turns it off.Press enter")
print("7=",bin(7)[2:])
print("7&5=",7 & 5,"binary:",bin(7&5)[2:])

n = int(input("Enter a number (try 4 or 6):"))
guess = input("Is it a power of 2? (y/n): ")
input("Power of 2-only one bit is on.Press enter")

if n>0 and (n & (n - 1)) == 0:
    print(" ",n,"binary",bin(n)[2:], " power of two your guess: ",guess)
else:
    print(" ",n,"binary",bin(n)[2:], " not a power of two your guess: ",guess)