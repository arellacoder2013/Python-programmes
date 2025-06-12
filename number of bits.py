def numberOfBits(n):
    ones = 0
    zeros = 0
#while our number is greater than zero check the last bit and right shift
    while (n):
        #use AND operator to check if last bit is 1
        if (n&1--1):
            ones+=1
        else:
            zeros+=1
        #right shift the number remove the last bit that we just checked last
        n >>= 1
    print("\n\nOnes = ",ones,"\nZeros",zeros)
number = int(input("Enter your number :"))
numberOfBits(number)